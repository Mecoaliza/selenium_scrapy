from src.login import iniciar_driver, login_cyber
import os
from dotenv import load_dotenv
from src.banco import executar_vql

load_dotenv()

vql = """
SELECT 
    nome, atraso, saldo_vencido, ds_produto, contrato 
FROM 
    base_inadimplentes 
WHERE 
    cod_cooperativa = '0001' 
    AND atraso > 90 
    AND saldo_vencido > 20000 
    AND flg_bloqueio = 'N' 
    AND prejuizo = 'N' 
CONTEXT ('I18N' = 'pt_br2')
"""

usuario = os.getenv("USUARIO_SISTEMA")
senha = os.getenv("SENHA_SISTEMA")

driver = iniciar_driver()
sucesso = login_cyber(driver, usuario, senha)
if not sucesso:
    print("Encerrando script por falha no login.")
    exit()
df = executar_vql(vql)
print(f"Total de registros encontrados: {len(df)}")



