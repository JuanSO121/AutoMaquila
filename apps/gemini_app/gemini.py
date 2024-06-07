# apps/gemini_app/gemini.py

import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import json

load_dotenv()

class geminiApi:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = None

    def configure(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name="gemini-pro-vision")
        return self.model

    def extract_order_details(self, file_path):
        """
        Extrae detalles del pedido de una imagen.
        """
        # Abre la imagen y define el prompt.
        imagen = Image.open(file_path)
        prompt = """
        Extrae los detalles del pedido de la imagen en el siguiente formato:
        {
            "numero_pedido": "123456",
            "bloque": "A",
            "tipo_servicio": "pegado",
            "fecha_pedido": "2024-06-01",
            "fecha_entrega": "2024-06-10",
            "cliente": "Cliente XYZ",
            "referencia_calzado": "Referencia123",
            "lista_pares": [{"modelo": "XYZ", "cantidad": 10}, {"modelo": "ABC", "cantidad": 20}],
            "total_pares": 30
        }
        """
        
        response = self.model.generate_content([prompt, imagen])
        
        if response and hasattr(response, 'text'):
            extracted_text = response.text
            print("Texto extraído de la imagen:")
            print(extracted_text)
            try:
                # Intenta parsear el texto extraído como JSON.
                order_details = json.loads(extracted_text)
            except json.JSONDecodeError:
                # Si el JSON no es válido, intentar parsear manualmente.
                order_details = self.parse_order_details(extracted_text)
            
            return order_details
        else:
            raise ValueError("No se pudo extraer la información del pedido de la imagen.")
        
    def parse_order_details(self, text):
        """
        Parsea el texto extraído de la imagen y lo convierte en un diccionario con los datos del pedido.
        """
        lines = text.split('\n')
        order_details = {}
        current_key = None

        for line in lines:
            if ': ' in line:
                key, value = line.split(': ', 1)
                order_details[key.strip()] = value.strip()
                current_key = key.strip()
            elif current_key:
                order_details[current_key] += ' ' + line.strip()
        
        return order_details
