## Sistemas de informação - Classificação e Pesquisa de Dados - AMF

# CRAWLER DE JOGOS DA EPIC GAMES STORE

Este é um programa Python que coleta dados de jogos da Epic Games Store, especificamente da seção "Top Sellers". O programa utiliza Selenium para automatizar o navegador e extrair informações como o nome dos jogos e seus preços.

## Funcionalidades

O jogo possui um menu que contém as seguintes opções:

### 1. COLETAR DADOS
Coleta dados de jogos da página de top sellers da Epic Games Store e armazena as informações em uma lista.

### 2. MOSTRAR DADOS
Exibe os jogos coletados juntamente com seus preços.

### 3. ORDENAR DADOS COM HEAP SORT
Ordena os jogos coletados com base em seus preços utilizando o algoritmo Heap Sort.

### 4. SAIR
Finaliza o programa.

## CÓDIGO

### Estrutura do Código

O código é estruturado em várias funções principais:

- **`extrair()`**: Coleta os dados dos jogos. Utiliza Selenium para abrir a página dos top sellers e extrair informações relevantes.
- **`organizar(jogo)`**: Organiza os dados extraídos em um dicionário contendo o nome do jogo e seu preço.
- **`mostrar_dados(lst)`**: Exibe os dados dos jogos coletados.
- **`converter_float(valor)`**: Converte o preço do jogo de string para float, facilitando operações matemáticas.
- **`heapify_min(seq, n, i)`**: Função auxiliar para o algoritmo de ordenação Heap Sort, que organiza a lista de jogos com base em seus preços.
- **`heap_sort_min(seq)`**: Implementa o algoritmo Heap Sort para ordenar a lista de jogos.
- **`main()`**: Função principal que apresenta o menu e gerencia as interações do usuário.

### Como Funciona

1. O programa utiliza a biblioteca Selenium para abrir o navegador e acessar a página dos top sellers da Epic Games Store.
2. Após alguns segundos de carregamento, ele coleta os dados dos jogos, incluindo nome e preço.
3. Os dados são organizados em um dicionário e armazenados em uma lista.
4. O usuário pode então visualizar os dados, ordenar a lista de jogos com o alogoritmo de ordenação heap sort com base no preço e sair do programa.

### Requisitos
- Selenium

## AUTORES
Bernardo

José Arcangelo
