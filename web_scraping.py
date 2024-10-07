from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

def extrair():
  """Coleta os dados que se é desejado."""
  url = "https://store.epicgames.com/pt-BR/collection/top-sellers"

  # Inicializa um novo serviço para o ChromeDriver
  service = Service()
  # Permite definir opções para o navegador Chrome,
  options = webdriver.ChromeOptions()

  #Cria uma nova instancia no navegador usando o serviço e as opções definidas anteriormente.
  driver = webdriver.Chrome(service = service, options = options)
  driver.get(url)
  
  sleep(3)
  os.system('cls')
  print("Carregando...")
  lista_jogos = driver.find_elements(By.CLASS_NAME, 'css-g3jcms')
  
  lst = []
  for elemento in lista_jogos:
    jogo = elemento.text
    print(elemento.text)
    jogo = jogo.split("\n")
    lst.append(organizar(jogo))
  
  driver.quit()

  print("\n\n::::DADOS COLETADOS COM SUCESSO!::::")
  return lst
  
def organizar(jogo):
  """Organizado os dados que serão usados, em dicionários."""
  jogo_dic = {}
  jogo_dic["Nome do jogo"] = jogo[1]
  jogo_dic["Preco"] = jogo[-1]
      
  return jogo_dic

def mostrar_dados(lst):
  """Exibi os jogos e seus preços."""
  print("\n::::::::::::::::::::::::")
  for i in lst:
    print("Nome do jogo: " + i["Nome do jogo"] + " Valor do jogo: " + i["Preco"] + "\n")
  print("::::::::::::::::::::::::\n")

def converter_float(valor):
  """Converte o preço do jogo, que está em String, para float."""
  valor = valor.replace("R$ ", "")
  valor = valor.replace(",", ".")
  valor = float(valor)
  return valor

def heapify_min(seq, n, i):
    menor = i  
    elemento_esquerda =2 * i + 1  
    elemento_direita = 2 * i + 2

    if elemento_esquerda < n:
      valor_esq = converter_float(seq[elemento_esquerda]["Preco"])
      valor_menor = converter_float(seq[menor]["Preco"])

      if valor_esq < valor_menor:
          menor = elemento_esquerda

    if elemento_direita < n:
      valor_dir = converter_float(seq[elemento_direita]["Preco"])
      valor_menor = converter_float(seq[menor]["Preco"])
      
      if elemento_direita < n and valor_dir < valor_menor:
          menor =elemento_direita

    if menor != i:
        seq[i], seq[menor] = seq[menor], seq[i]  
        heapify_min(seq, n, menor)  

def heap_sort_min(seq):
    n = len(seq)

    for i in range(n //2-1,-1,-1):
        heapify_min(seq, n, i)
    
    for i in range(n-1,0,-1):
        seq[i], seq[0] = seq[0], seq[i]
        heapify_min(seq, i, 0)

def gerar_arquivo_inicial(nome_arquivo, lst):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for jogo in lst:
          nome = jogo["Nome do jogo"]
          preco = jogo["Preco"]
          arquivo.write(f"{nome}; {preco}\n")

def main():
  while True:
    print("::::CRAWLER::::" + "\n1- COLETAR DADOS" + "\n2- MOSTRAR DADOS" + "\n3- ORDENAR DADOS COM HEAP SORT" + "\n4- SAIR")
    opc = input("Informe a opção desejada: ")

    if opc == "1":
      os.system('cls')
      lst = extrair()
      gerar_arquivo_inicial("large.txt", lst)

    elif opc == "2":
      os.system('cls')
      mostrar_dados(lst)

    elif opc == "3":
      os.system('cls')
      heap_sort_min(lst)
      lst.reverse()
      print("::::DADOS ORDENADOS COM SUCESSO!::::")

    elif opc == "4":
      os.system('cls')

      print("Saindo...")
      break
  
    else:
      os.system('cls')
      print("::::VALOR INVÁLIDO!::::")

main()
