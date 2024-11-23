# Script para probar la conexión e imprimir el listado de modelos de  OpenAI disponibles
import os
import openai
import logging
from dotenv import load_dotenv
from prettytable import PrettyTable

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Carga variables de entorno desde el archivo .env
load_dotenv()

# Carga api key de OpenAI desde el archivo .env
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.info("Cargando Api Key de OpenAI")

# Realizar una solicitud simple de prueba a la API
try:
    models = openai.Model.list()
    logging.info("Api Key correcta - Conexión establecida con OpenAI")
    table = PrettyTable()
    table.field_names = ["Model ID", "Model Name"]

    for model in models['data']:
        model_id = model['id']
        model_name = model.get('display_name', 'N/A')
        table.add_row([model_id, model_name])

    logging.info(f"\n {table}")
except openai.error.AuthenticationError:
    logging.error("La ApiKey proporcionada es inválida.")
    exit(1)
except openai.error.OpenAIError as e:
    logging.error(f"No se pudo conectar con la API: {e}")
    exit(1)
finally:
    logging.info("============================================")
    logging.info("             Fin de la ejecución.")
