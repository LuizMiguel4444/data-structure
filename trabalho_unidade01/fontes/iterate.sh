#!/bin/sh

help="
SYNTAX:
$0 <executions> <size-start> <size-pass> <size-end> <program> <name>

  <executions> - number of program execution iterations
  <size-start> - initial value of 'n' (size of the problem instance)
  <size-pass>  - increment value of 'n' (size of the problem instance)
  <size-end>   - final value of 'n' (size of the problem instance)
  <program>    - program string (name plus additional arguments)
  <name>       - base string used to create filenames
"

if [ $# -eq 6 ]; then

    result=$6.txt
    echo -n > $result

    for n in `seq $2 $3 $4`;
    do
        file=$6-$1-$n.txt
        echo -n > $file

        for i in `seq $1`;
        do
            $5 $n >> $file
        done

        max=$(awk 'BEGIN{s=0} {if ($1>s) s=$1} END{printf "%.2f", s}' $file)
        min=$(awk 'BEGIN{s='$max'} {if ($1<s) s=$1} END{printf "%.2f", s}' $file)
        mean=$(awk '{s+=$1} END{printf "%.2f", s/NR}' $file)
        maer=$(awk -v mean=$mean '{s+=($1-mean)^2} END{printf "%.2f", sqrt(s/NR)}' $file)

        echo "$n $mean $maer $max $min $1 $file" >> $result
    done
else
    echo "$help"
fi
