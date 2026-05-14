from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

api_key = os.getenv("API_KEY")


client = OpenAI(api_key = api_key)

def car_ai_bio(model, brand, year):
    prompt = f'Escreva uma curta biografia para um carro com as seguintes características: Modelo: {model}, Marca: {brand}, Ano: {year}. O texto deve ter no máximo 250 caracteres, e limpo para publicação no sistema.'
    
    response = client.responses.create(
        model='gpt-5.4-mini',
        input=prompt,
        )

    return response.output_text
