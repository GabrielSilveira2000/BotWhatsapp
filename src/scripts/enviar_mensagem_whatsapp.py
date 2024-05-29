from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from encontrar_elemento import Elemento
from selenium import webdriver
from time import sleep
import os


caminho_raiz = os.getcwd()

chrome_profile_path = f"{caminho_raiz}\profile"
service = Service(ChromeDriverManager().install())

# Configurando as opções do Chrome para usar o perfil
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

# Iniciando o driver do Chrome com o perfil configurado
navegador = webdriver.Chrome(service=service, options=options)

# Acessando o WhatsApp Web
navegador.get('https://web.whatsapp.com/')
    

def enviar(contatos:list, mensagens:list, arquivos:list):
    contato_anterior = ""
    for i,(contato, mensagem, arquivo) in enumerate(zip(contatos, mensagens, arquivos)):
        
        if(contato_anterior == "" or not contato_anterior == contato):
            
            Elemento(navegador, By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div', Digitar=contato)
            Elemento(navegador, By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]', Submit=False)
            contato_anterior = contato
            
        if(arquivo):
            Elemento(navegador, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span', Submit=False)
            upload_element = Elemento(navegador, By.CSS_SELECTOR, 'input[type="file"]', Obter_Elemneto=True)
            file_path = f'{caminho_raiz}\\arquivos\{arquivo}'
            upload_element.send_keys(file_path)
            Elemento(navegador, By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div', Submit=False)
        
        sleep(3)
        
        if mensagem:
            Elemento(navegador, By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]", Submit=False)
            Elemento(navegador, By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]", Digitar=mensagem)
            Elemento(navegador, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button', Submit=False)
        
        if i < len(contatos):
            sleep(3)
            
    return "Todas as mensagems foram enviadas"
    