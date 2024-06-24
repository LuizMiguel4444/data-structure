# README

Este repositório é destinado ao trabalho da primeira unidade da disciplina de Estrutura de Dados. Nele contém os algorítmos de ordenação requeridos, os resultados e gráficos, além do relatório destinado à análise dos mesmos. Neste arquivo README, você encontrará instruções sobre como configurar o ambiente virtual e executar os programas.

## Sobre os algorítmos

Dentro do arquivo de cada algorítmo existem funções que criam vetores, podendo ser aleatórios ou não, de acordo com o melhor e pior caso, caso exista. Eles servem para testar os algorítmos em todos os seus possíveis casos. Nos arquivos de cada algorítmo existem linhas comentadas que sinalizam qual vetor está sendo usado para induzir o programa a executar o caso desejado. Caso queira, você pode alterar o caso em questão apenas comentadando e descomentandos algumas linhas.

## Configurando o Ambiente Virtual

1. Certifique-se de ter o Python instalado em sua máquina, em sua versão mais recente. Você pode fazer o download em https://www.python.org/downloads/.

2. Abra o terminal ou prompt de comando e navegue até o diretório /trabalho_unidade01/fontes.

3. Crie um ambiente virtual executando o seguinte comando:

```bash
python3 -m venv nome_do_ambiente
```

4. Ative o ambiente virtual:

- No Linux e macOS:
```bash
source nome_do_ambiente/bin/activate
```

- No Windows:
```bash
nome_do_ambiente\Scripts\activate
```

## Executando os programas

Após configurar o ambiente virtual, siga os passos abaixo para executar os programas:

1. No terminal ou prompt de comando, certifique-se de estar no diretório citado acima.

2. Escolha um dos algorítmos, seguido pelo tamanho do vetor desejado. Por exemplo:

```bash
python3 quick.py 1000
```

3. O programa será executado e exibirá o tempo em nano segundos em que foi executado.

## Executando com o iterate

O script iterate.sh só pode ser executado em terminal Linux ou usando o WSL no Windows. O iterate irá interagir com os scripts python gerando vetores com os resultados e os salvando em arquivos txt.

### Sintaxe para executar o iterate:

Rótulo                       | Explicação
:--------------------------- | :-------------------------------------------------------------
Execuções                    | Número de iterações de execução do programa
Tamanho_inicial              | Valor inicial de 'n' (tamanho da instância do problema)
Aumento_a_cada_iteração      | Valor de incremento de 'n' (tamanho da instância do problema)
Tamanho_final                | Valor final de 'n' (tamanho da instância do problema)
Nome_do_programa             | String do programa (nome mais argumentos adicionais)
Nome_do_arquivo_final        | Nome para a criação do arquivo com os resultados

1. Ainda no diretório /trabalho_unidade01/fontes utilize a seguinte sintaxe de comando no terminal.

```bash
./iterate.sh execuções tamanho_inicial aumento_a_cada_iteração tamanho_final "python3 nome_do_programa.py" nome_do_arquivo_final
```

2. Exemplo:

```bash
./iterate.sh 50 100 100 900 "python3 quick.py" resultados_quick
```