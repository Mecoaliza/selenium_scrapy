import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def acessar_cyber_branch(driver):

    driver.get("http://cyber.net/bei010Web")
    elemento = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='CyberBranch']"))
    )
    elemento.click()
    time.sleep(3)
    print("Acesso à CyberBranch realizado com sucesso.")

def buscar_usuario_por_nome(driver, nome_usuario: str):

    select_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "searchType"))
    )
    select = Select(select_box)
    select.select_by_visible_text("Nome")

    campo_nome = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "searchParam"))
    )
    campo_nome.send_keys(nome_usuario)

    botao_executar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Executar')]"))
    )
    botao_executar.click()
    print(f"🔍 Usuário '{nome_usuario}' buscado com sucesso.")



def preencher_campos_ca_cr(driver):

    xpath_ca = "//input[@maxlength='2' and not(@disabled)]"
    ca_campo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_ca))
    )
    ca_campo.send_keys('EN')
    ca_campo.send_keys(Keys.ENTER)
    time.sleep(2)

    xpath_cr = "(//input[@maxlength='2' and not(@disabled)])[2]"
    cr_campo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_cr))
    )
    cr_campo.send_keys('EN')
    print("Campos CA e CR preenchidos com sucesso.")

def clique_notificacao(driver):

    try:
        botao_ok = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ok"))
        )
        botao_ok.click()
        print("✅ Botão 'OK' clicado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao clicar no botão OK: {e}")