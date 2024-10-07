import heapq
import os

# Função para converter o preço de string para float
def extrair_preco(texto):
    preco_str = texto.split("; R$ ")[1]  # Pega a parte do preço
    return float(preco_str.replace(",", "."))

# Função para mesclar arquivos temporários com ordenação baseada no preço.
def mesclar_arquivo():
    saida = []
    heap = []
    memoria = [[], [], [], [], []]

    # Criar array de manipuladores de arquivo
    manipuladores_arquivo = [0] * 5
    for i in range(5):
        arquivo = f'{i}.txt'
        if os.path.exists(arquivo):
            f = open(arquivo, "r", encoding='utf-8')
            manipuladores_arquivo[i] = (i, f)
        else:
            manipuladores_arquivo[i] = (i, None)  # Nenhum arquivo existe

    # Ler as primeiras 100 linhas de todos os arquivos na memória
    for i in range(5):
        if manipuladores_arquivo[i][1]:  # Verifica se o arquivo está aberto
            for j in range(100):
                linha = manipuladores_arquivo[i][1].readline()
                if linha:  # Verifica se a linha existe
                    memoria[i].append(linha.strip())

    # Inicializa o heap com o primeiro valor de todas as partes da memória, baseado no preço
    for i in range(len(memoria)):
        if memoria[i]:  # Verifica se a memória não está vazia
            heapq.heappush(heap, (extrair_preco(memoria[i][0]), memoria[i][0], i))

    # Loop até que o heap esteja vazio
    while heap:
        _, valor, indice_memoria = heapq.heappop(heap)
        saida.append(valor)

        # Se a memória correspondente não estiver vazia
        if memoria[indice_memoria]:
            memoria[indice_memoria].pop(0)  # Remove o primeiro elemento
            if memoria[indice_memoria]:  # Se ainda houver elementos, adicione o próximo ao heap
                heapq.heappush(heap, (extrair_preco(memoria[indice_memoria][0]), memoria[indice_memoria][0], indice_memoria))
            else:
                # Ler mais linhas se a memória estiver vazia
                linha = manipuladores_arquivo[indice_memoria][1].readline()
                if linha:  # Verifica se a linha existe
                    memoria[indice_memoria].append(linha.strip())
                    heapq.heappush(heap, (extrair_preco(memoria[indice_memoria][0]), memoria[indice_memoria][0], indice_memoria))

        # Se a saída atingir 100 linhas, escreva em um arquivo e limpe a saída
        if len(saida) == 100:
            with open("ordenado.txt", "a", encoding='utf-8') as arquivo:
                for i in saida:
                    arquivo.write(i + '\n')
            saida = []

    # Escreve qualquer restante no arquivo
    if saida:
        with open("ordenado.txt", "a", encoding='utf-8') as arquivo:
            for i in saida:
                arquivo.write(i + '\n')

    # Fecha todos os arquivos abertos
    for i in range(5):
        if manipuladores_arquivo[i][1]:
            manipuladores_arquivo[i][1].close()

# Função de divisão e ordenação por preço
def dividir_arquivo(nome_arquivo):
    contador = 0
    dados = []

    # Contando o total de linhas no arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        total_linhas = sum(1 for _ in f)

    # Calculando o tamanho do chunk
    tamanho_chunk = total_linhas // 5 + 1

    # Abrindo o arquivo grande novamente para leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as manipulador_arquivo_grande:
        while total_linhas > 0:
            if total_linhas < tamanho_chunk:
                tamanho_chunk = total_linhas

            # Lendo as linhas e armazenando em uma lista
            dados = [next(manipulador_arquivo_grande).strip() for _ in range(tamanho_chunk)]
            dados.sort(key=extrair_preco)  # Ordenando as linhas por preço

            # Abrindo o arquivo temporário e escrevendo as linhas
            nome_arquivo_pequeno = f"{contador}.txt"
            with open(nome_arquivo_pequeno, "w", encoding='utf-8') as arquivo_temp:
                for linha in dados:
                    arquivo_temp.write(linha + '\n')

            contador += 1
            total_linhas -= tamanho_chunk  # Atualiza o total de linhas restantes
            dados = []  # Limpa a lista de dados

def main():
    nome_arquivo_grande = "large.txt"  # Certifique-se de que este arquivo exista
    # Chamando a função de divisão para criar arquivos temporários ordenados
    dividir_arquivo(nome_arquivo_grande)
    # Função para mesclar arquivos temporários
    mesclar_arquivo()

main()
