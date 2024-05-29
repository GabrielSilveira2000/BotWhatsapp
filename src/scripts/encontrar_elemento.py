from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unidecode import unidecode
from selenium import webdriver
import time

navegador = webdriver.Chrome()

def Elemento(Navegador_Instaciado:webdriver.Chrome, Tipo_Elemento:By, Nome_Tipo:str, Digitar:str='', Submit: bool = False, Scrolar_Pagina:str= "", HTML:bool=False, Encontrado=False, Tempo_Scroll= 10, Obter_Elemneto:bool =False):
    try:
        if(not Encontrado):
            time.sleep(0.1)
            elemento = Navegador_Instaciado.find_element(Tipo_Elemento, Nome_Tipo)
            Encontrado = True
            if(Obter_Elemneto):
                return elemento
            if(Scrolar_Pagina == ""):

                if (Digitar != ""):
                    elemento.click()
                    actions = ActionChains(Navegador_Instaciado, 0.2)
                    for char in Digitar:
                        actions.send_keys(char).perform()
                        Tempo_Escrever = random.uniform(0.00001, 0.000003)
                        time.sleep(Tempo_Escrever)
                else:
                    if (HTML):
                        return str(elemento.text)
                    else:
                        if Submit:
                            elemento.submit()
                        else:
                            elemento.click()
            else:
                Navegador_Instaciado.execute_script(f"window.scrollTo(0, {Scrolar_Pagina});")
                time.sleep(Tempo_Scroll)
                
    except:
        if(not Encontrado):
            time.sleep(0.5)
            Elemento(Navegador_Instaciado, Tipo_Elemento, Nome_Tipo, Digitar, Submit, Scrolar_Pagina, HTML, Encontrado, Tempo_Scroll, Obter_Elemneto)