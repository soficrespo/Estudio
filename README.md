RAG de Estudio

¿Que es?

Es un asistente de estudio que permite subir archivos (PDF o Word) y hacer preguntas basadas únicamente en esos documentos, usando la API de Gemini para generar embeddings y respuestas.

¿Cómo funciona?

1.Subís un documento (PDF o Word)

2.El texto se extrae y se divide en fragmentos (chunks)

3.Cada fragmento se convierte en un embedding (vector numérico) con la API de Gemini

4.Los embeddings se guardan localmente en una base de datos vectorial (ChromaDB)

5.Al hacer una pregunta, se busca qué fragmentos son más relevantes y se los pasa a Gemini como contexto para generar la respuesta

Requisitos
Python 3.10 o superior
Una API key gratuita de Gemini 

Instalación
1.Clona el repositorio 
  git clone https://github.com/soficrespo/Estudio.git
  cd Estudio
2.Creá y activá un entorno virtual:
  python -m venv venv
3.Instalá las dependencias
  pip install -r requirements.txt
4.Creá un archivo .env en la raíz del proyecto con tu propia API key
  Con este formato: GEMINI_API_KEY=tu_clave_aca

Notas
El nivel gratuito de la API de Gemini tiene límites de requests por minuto/día, suficientes para uso personal de estudio
La extracción de texto de PDFs escaneados (imágenes) no funciona, ya que no se aplica OCR
