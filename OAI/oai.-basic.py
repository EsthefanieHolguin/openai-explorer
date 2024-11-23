# Script con promt básico para generar un poema sobre recursividad en programación
import os
import openai
import logging
from dotenv import load_dotenv

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Carga variables de entorno desde el archivo .env
load_dotenv()

# Carga api key de OpenAI desde el archivo .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("No se encontró la clave API de OpenAI en el archivo .env\n")
    exit(1)

#Genera promt para solicitar un poema sobre recursividad en programación
try:
    response = openai.ChatCompletion.create(
        model="davinci-002",
        messages=[
            {"role": "system", "content": "Eresun asistente de poesía."},
            {"role": "user", "content": "Compón un poema que  explique el Concepto de recursividad en programación.."},
        ]
    )

    #Imprime respuesta generada por la API
    print(response.choices[0].message['content'].strip())

except openai.error.OpenAIError as e:
    if e.code == 'insufficient_quota':
        logging.error("\nHas excedido tu cuota actual. Revisa tu plan y detalles de facturación.")
    else:
        logging.error(f"\nError al conectar con la API de OpenAI: {e}")



# Fin del script
logging.info("Fin de la ejecución.")
