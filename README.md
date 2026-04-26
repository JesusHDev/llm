Proyecto 7: LLM - AlphaBot (Vulcan Hardware) 
Este proyecto consiste en el diseño e implementación de un asistente técnico de inteligencia artificial (AlphaBot) que opera de forma 100% local. El sistema utiliza una arquitectura híbrida para garantizar respuestas precisas, seguras y de baja latencia en hardware de recursos moderados.

Arquitectura del Sistema (Defensa en Profundidad)
Para mitigar las alucinaciones y el consumo excesivo de recursos, se implementó una estructura de tres capas:

Capa 1: Filtro Heurístico (Python): Intercepta peticiones no relacionadas con hardware (fútbol, cocina, etc.) mediante un análisis de palabras clave, evitando el gasto innecesario de ciclos de CPU.

Capa 2: Retrieval-Augmented Generation (RAG): Inyecta una "Fuente de Verdad" mediante un archivo de base de conocimientos (base_conocimientos.txt). Esto obliga al modelo a responder basándose en datos reales y no en su entrenamiento estadístico.

Capa 3: Inferencia Determinista: Uso del modelo TinyLlama (1.1B) con una configuración de temperature: 0 para eliminar la creatividad aleatoria y asegurar respuestas técnicas consistentes.

 Optimización de Hardware (Edge Computing)El sistema ha sido refinado para ejecutarse con fluidez en procesadores de alta eficiencia (como el Intel N95), optimizando los siguientes parámetros:Tokens Per Second (TPS): Maximizado mediante la reducción del tamaño del modelo a 1.1B parámetros.Time to First Token (TTFT): Optimizado mediante el uso de prompts atómicos y limpieza de ruido en el contexto.Ancho de banda de memoria: Reducción de la carga en RAM (aprox. 600MB de uso) para evitar el cuello de botella del procesador.

 Instalación y Configuración
1. Requisitos Previos
Ollama instalado y operativo.

Modelo descargado: ollama pull tinyllama.

2. Estructura de Archivos

.
├── atencion_cliente.py     # Lógica principal del sistema
├── base_conocimientos.txt  # Datos técnicos reales (Fuente de Verdad)
├── .env                    # Configuración de variables de entorno
├── .gitignore              # Protección de archivos sensibles
└── venv_llm/               # Entorno virtual de Python

3. Configuración del Entorno

# Crear y activar entorno virtual
python3 -m venv venv_llm
source venv_llm/bin/activate

# Instalar dependencias
pip install ollama python-dotenv

4. Variables de Entorno (.env)

MODEL_NAME=tinyllama

Uso
Ejecuta el script principal para iniciar el servicio local:

python3 atencion_cliente.py

Seguridad
El proyecto implementa un archivo .gitignore robusto que evita la subida de entornos virtuales y archivos de configuración personal (.env), siguiendo las mejores prácticas de seguridad en el desarrollo de software.
