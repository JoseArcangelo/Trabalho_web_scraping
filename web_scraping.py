from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

def extrair():
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
 
  for jogo in lista_jogos:
    j = jogo.text
    j = j.split("\n")
    jogo_obj = transformar(j)
    lst.append(jogo_obj)
  
  driver.quit()
  os.system('cls')
  print("DADOS COLETADOS COM SUCESSO!")
  return lst
  
def transformar(jogo): 
  jogo_obj = {}
  jogo_obj["Nome do jogo"] = jogo[1]
  jogo_obj["Preco"] = jogo[-1]
      
  return jogo_obj

def mostrar_dados(lst):
  for i in lst:
    print("Nome do jogo: " + i["Nome do jogo"] + "\nValor do jogo: " + i["Preco"] + "\n")

def converter(valor):
  valor = valor.replace("R$ ", "")
  valor = valor.replace(",", ".")
  valor = float(valor)
  return valor


def heapify_min(seq, n, i):
    menor = i  
    elemento_esquerda =2 * i + 1  
    elemento_direita = 2 * i + 2

    if elemento_esquerda < n:
      valor_esq = converter(seq[elemento_esquerda]["Preco"])
      valor_menor = converter(seq[menor]["Preco"])

      if valor_esq < valor_menor:
          menor =elemento_esquerda

    if elemento_direita < n:
      valor_dir = converter(seq[elemento_direita]["Preco"])
      valor_menor = converter(seq[menor]["Preco"])
      
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


def main():
  while True:
    print("1- COLETAR DADOS" + "\n2- MOSTRAR DADOS" + "\n3- ORDENAR DADOS COM HEAP SORT" + "\n4- ORDENAR DADOS COM MERGESORT EXTERNO" + "\n5- SAIR")
    opc = input("Informe a opção desejada: ")
    os.system('cls')
    if opc == "1":
      lst = extrair()
      
    elif opc == "2":
      mostrar_dados(lst)
  
    elif opc == "3":
      heap_sort_min(lst)
      lst.reverse()
      print("DADOS ORDENADOS COM SUCESSO!")

    elif opc == "5":
      print("Saindo...")
      break
      
    else:
      print("VALOR INVÁLIDO!")

main()



