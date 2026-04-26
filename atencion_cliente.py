import ollama
import os
from dotenv import load_dotenv

load_dotenv()
MODELO = os.getenv("MODEL_NAME", "tinyllama")

def chat_atencion():
    # Cargamos la base optimizada
    with open("base_conocimientos.txt", "r") as f:
        datos = f.read()

    # PROMPT DE ALTA VELOCIDAD: Instrucciones atómicas
    SYSTEM_ROLE = f"Eres AlphaBot. DATOS: {datos}. REGLA: Responde corto usando solo los DATOS. Si no está en DATOS, di 'No disponible'."

    print(f"--- 🚀 VULCAN FAST-MODE (Motor: {MODELO}) ---")
    
    while True:
        pregunta = input("\nUsuario: ")
        if pregunta.lower() in ["salir", "exit"]: break

        # Filtro de seguridad rápido
        if any(p in pregunta.lower() for p in ["pizza", "futbol", "receta"]):
            print("AlphaBot: Solo hardware.")
            continue

        try:
            # Quitamos 'stream=True' para que la CPU procese el bloque completo más rápido
            response = ollama.chat(
                model=MODELO,
                messages=[
                    {'role': 'system', 'content': SYSTEM_ROLE},
                    {'role': 'user', 'content': pregunta}
                ],
                options={'temperature': 0, 'num_predict': 50} # Limitamos la longitud de respuesta
            )
            print(f"AlphaBot: {response['message']['content'].strip()}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_atencion()
