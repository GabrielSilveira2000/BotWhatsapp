from encontrar_elemento import Elemento
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
Elemento(navegador, By.XPATH, "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div/div[2]", Submit=False)
Elemento(navegador, By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]", Submit=False)
Elemento(navegador, By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]", Digitar="teste")
sleep(15)