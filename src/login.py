from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def iniciar_driver():
    driver = webdriver.Edge()
    return driver

def login_cyber(driver, usuario: str, senha: str):
    
    driver.get('http://cyber.net/')

    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, "topFrame"))
        )

        campo_usuario = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "fieldUser"))
        )
        campo_usuario.send_keys(usuario)

        campo_senha = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "fieldPassword"))
        )
        campo_senha.send_keys(senha)

        botao_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSubmit"))
        )

        botao_login.click()

        print(" Login realizado com sucesso.")
        return True
    except Exception as e:
        print(f"Falha no login: {e}")
        return False

