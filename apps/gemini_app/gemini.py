# gemini_app/gemini.py
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

    def configure_2(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name="gemini-pro")
        return self.model
    
    def extract_order_data(self, file_path):
        """
        Procesa una imagen de una hoja de pedidos y extrae los datos relevantes.
        """
        imagen = Image.open(file_path)
        prompt = "Extrae los datos de los pedidos de esta imagen de hoja de pedidos. Devuélvelos en formato JSON con los campos: numero_pedido, bloque, tipo_servicio, fecha_pedido, fecha_entrega, cliente, referencia_calzado, lista_pares, total_pares."
        
        # Suponiendo que la API admite tanto texto como imágenes como entrada
        response = self.model.generate_content([prompt, imagen])
        
        # Asumimos que la API devuelve un JSON con los datos relevantes
        if response and response.text:
            try:
                order_data = json.loads(response.text)
                return order_data
            except json.JSONDecodeError:
                print("No se pudo decodificar la respuesta como JSON.")
                return None
        return None
