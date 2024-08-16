# README

Este repositório é destinado ao trabalho da segunda unidade da disciplina de Estrutura de Dados. Nele contém os algorítmos de ávores binárias e tabela de dispersão requeridos, os resultados e gráficos, além do relatório destinado à análise dos mesmos. Neste arquivo README, você encontrará instruções sobre como executar os programas.

## Sobre os algorítmos

Dentro do arquivo de cada algorítmo existem funções que criam vetores, podendo ser aleatórios ou não, de acordo com o melhor e pior caso, caso exista. Eles servem para testar os algorítmos em todos os seus possíveis casos. Nos arquivos de cada algorítmo existem linhas comentadas que sinalizam qual vetor está sendo usado para induzir o programa a executar o caso desejado. Caso queira, você pode alterar o caso em questão apenas comentadando e descomentandos algumas linhas.

## Executando os programas

Siga os passos abaixo para executar os programas:

1. No terminal ou prompt de comando, certifique-se de estar no diretório citado acima.

2. Compile o código com os seguintes comandos: gcc -c -Wall arquivo.c

3. Gere o executavel com o comando: gcc -o executal arquivo.o

4. Escolha um dos algorítmos, seguido pelo tamanho do vetor desejado. Por exemplo:

```bash
./programa 1000
```

5. O programa será executado e exibirá o tempo em nano segundos em que foi executado.

## Executando com o iterate

O script iterate.sh só pode ser executado em terminal Linux ou usando o WSL no Windows. O iterate irá interagir com os scripts gerando vetores com os resultados e os salvando em arquivos txt.

### Sintaxe para executar o iterate:

Rótulo                       | Explicação
:--------------------------- | :-------------------------------------------------------------
Execuções                    | Número de iterações de execução do programa
Tamanho_inicial              | Valor inicial de 'n' (tamanho da instância do problema)
Aumento_a_cada_iteração      | Valor de incremento de 'n' (tamanho da instância do problema)
Tamanho_final                | Valor final de 'n' (tamanho da instância do problema)
Nome_do_programa             | String do programa (nome mais argumentos adicionais)
Nome_do_arquivo_final        | Nome para a criação do arquivo com os resultados

1. Ainda no diretório /trabalho_unidade02/fontes utilize a seguinte sintaxe de comando no terminal.

```bash
./iterate.sh execuções tamanho_inicial aumento_a_cada_iteração tamanho_final "nome_do_programa" nome_do_arquivo_final_txt
```

2. Exemplo:

```bash
./iterate.sh 50 100 100 900 "./programa" resultados_programa
```
