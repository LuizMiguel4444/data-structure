set terminal pngcairo size 800,600
set output 'output.png'
set grid
set title 'tempo de execução do algoritmo'
set ylabel "tempo em nanosegundos"
set xlabel "tamanho da instância do problema (n)"
plot 'nome_do_arquivo.txt' using 1:2 with linespoints title 'title' pointtype 0
