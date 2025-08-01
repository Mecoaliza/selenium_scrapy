from src.login import iniciar_driver, login_cyber
import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("USUARIO_SISTEMA")
senha = os.getenv("SENHA_SISTEMA")

driver = iniciar_driver()
sucesso = login_cyber(driver, usuario, senha)

if not sucesso:
    print("Encerrando script por falha no login.")
    exit()