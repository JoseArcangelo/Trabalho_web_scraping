import heapq
import os

def extrair_preco(texto):
    preco_str = texto.split("; R$ ")[1]  
    return float(preco_str.replace(",", "."))

def mesclar_arquivo():
    saida = []
    heap = []
    memoria = [[], [], [], [], []]

    manipuladores_arquivo = [0] * 5
    for i in range(5):
        arquivo = f'{i}.txt'
        if os.path.exists(arquivo):
            f = open(arquivo, "r", encoding='utf-8')
            manipuladores_arquivo[i] = (i, f)
        else:
            manipuladores_arquivo[i] = (i, None) 
    for i in range(5):
        if manipuladores_arquivo[i][1]:
            for j in range(100):
                linha = manipuladores_arquivo[i][1].readline()
                if linha:  
                    memoria[i].append(linha.strip())

    for i in range(len(memoria)):
        if memoria[i]:  
            heapq.heappush(heap, (extrair_preco(memoria[i][0]), memoria[i][0], i))

    while heap:
        _, valor, indice_memoria = heapq.heappop(heap)
        saida.append(valor)

        if memoria[indice_memoria]:
            memoria[indice_memoria].pop(0)  
            if memoria[indice_memoria]:  
                heapq.heappush(heap, (extrair_preco(memoria[indice_memoria][0]), memoria[indice_memoria][0], indice_memoria))
            else:

                linha = manipuladores_arquivo[indice_memoria][1].readline()
                if linha: 
                    memoria[indice_memoria].append(linha.strip())
                    heapq.heappush(heap, (extrair_preco(memoria[indice_memoria][0]), memoria[indice_memoria][0], indice_memoria))

        if len(saida) == 100:
            with open("ordenado.txt", "a", encoding='utf-8') as arquivo:
                for i in saida:
                    arquivo.write(i + '\n')
            saida = []

    if saida:
        with open("ordenado.txt", "a", encoding='utf-8') as arquivo:
            for i in saida:
                arquivo.write(i + '\n')

    for i in range(5):
        if manipuladores_arquivo[i][1]:
            manipuladores_arquivo[i][1].close()

def dividir_arquivo(nome_arquivo):
    contador = 0
    dados = []

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        total_linhas = sum(1 for _ in f)

    tamanho_chunk = total_linhas // 5 + 1

    with open(nome_arquivo, 'r', encoding='utf-8') as manipulador_arquivo_grande:
        while total_linhas > 0:
            if total_linhas < tamanho_chunk:
                tamanho_chunk = total_linhas

            dados = [next(manipulador_arquivo_grande).strip() for _ in range(tamanho_chunk)]
            dados.sort(key=extrair_preco) 

            nome_arquivo_pequeno = f"{contador}.txt"
            with open(nome_arquivo_pequeno, "w", encoding='utf-8') as arquivo_temp:
                for linha in dados:
                    arquivo_temp.write(linha + '\n')

            contador += 1
            total_linhas -= tamanho_chunk 
            dados = []  

def main():
    nome_arquivo_grande = "large.txt"  
    dividir_arquivo(nome_arquivo_grande)
    mesclar_arquivo()

main()
