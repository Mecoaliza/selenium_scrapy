import os
import time
import logging
import pandas as pd
import psycopg2 as dbdriver
from socket import gethostname
from dotenv import load_dotenv

load_dotenv()

USER_BANCO = os.getenv("USER_DB")
PASSWORD_BANCO = os.getenv("PASSWORD_DB")

def conectar_banco():
    try:
        conn_str = {
            'user': USER_BANCO,
            'password':PASSWORD_BANCO,
            'host': 'vitualizador.net',
            'dbname': 'ldw',
            'port': 9996
        }

        conn = dbdriver.connect(**conn_str)
        return conn
    except dbdriver.Error as e:
        logging.error(f"Erro ao conectar no banco de dados: {e}")
        return None
    
def executar_vql(vql: str, timeout: int = 30):
    conn = None
    start_time = time.time()

    try:
        conn = conectar_banco()

        if conn is None:
            raise Exception("Conexão combanco falhou.")
        
        cursor = conn.cursor()
        cursor.execute(vql)
        dados = cursor.fetchall()
        colunas = [desc.name for desc in cursor.description]

        df = pd.DataFrame(dados, columns=colunas)
        return df
    
    except Exception as e:
        logging.error(f"Erro ao executar VQL: {e}")

        return pd.DataFrame()
    
    finally:
        if conn:
            conn.close()
        elapsed = time.time() - start_time
        logging.info(f" Consulta executada em {elapsed:.2f} segundos.")
