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


def main():
  while True:
    print("1- COLETAR DADOS" + "\n2- MOSTRAR DADOS" + "\n3- ORDENAR DADOS")
    opc = input("Informe a opção desejada: ")
    if opc == "1":
      lst = extrair()
      os.system('cls')
      
    elif opc == "2":
      mostrar_dados(lst)
    
    else:
      break

main()
