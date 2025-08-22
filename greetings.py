import os
from datetime import datetime
from dotenv import load_dotenv

def mensaje_bienvenida():
    print("=" * 60)
    print("    🐳 CONTENEDOR DE BIENVENIDA 🐳")
    print("=" * 60)
    
    # Obtener variables de entorno si existen
    nombre = os.getenv('USUARIO_NOMBRE', 'Usuario')
    ambiente = os.getenv('AMBIENTE', 'github actions')
    
    print(f"¡Hola {nombre}!")
    print(f"Ambiente: {ambiente}")
    print(f"Hora de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Este script se está ejecutando dentro de un contenedor Docker.")
    print("¡Bienvenido a la containerización!")
    print("=" * 60)

if __name__ == "__main__":
    mensaje_bienvenida()