from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o navegador
navegador = webdriver.Chrome()

# Acessar o site
navegador.get("https://ligeirinhotransportes.atua.com.br/adm/")
time.sleep(3)

# Realizar login
navegador.find_element(By.NAME, "f_ds_apelido").send_keys("evandro")
navegador.find_element(By.NAME, "f_ds_senha").send_keys("awSoZCq9")
navegador.find_element(By.NAME, "f_ds_senha").send_keys(Keys.ENTER)
time.sleep(2)

# Fechar o navegador
navegador.quit()