from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

def extrair():
  url = "https://store.epicgames.com/pt-BR/collection/top-sellers"
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
  }

  service = Service()
  options = webdriver.ChromeOptions()

  driver = webdriver.Chrome(service = service, options = options)

  driver.get(url)
  
  sleep(3)
  os.system('cls')
  print("Carregando...")
  element_text = driver.find_elements(By.CLASS_NAME, 'css-g3jcms')
  lst = []

  for i in element_text:
    lst.append(i.text)
    lst.append("\n")

  driver.quit()
  lst = retirar_quebra_linha(lst)
  
  print("DADOS COLETADOS COM SUCESSO!")
      
  return lst
  
def retirar_quebra_linha(lst):
  for i in  range(len(lst)):
    lst[i] = lst[i].replace('\n', ' ')
  return lst

def mostrar_dados(lst):
  for i in lst:
    print(i)

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
