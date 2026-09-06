import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()
print("API Key encontrada:", os.getenv("GEMINI_API_KEY"))
clientGemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
clientChroma = chromadb.PersistentClient(path="./chroma_db")
collection = clientChroma.get_or_create_collection(name="Apuntes")

def generateEmbedding(text, taskType="RETRIEVAL_DOCUMENT"):
    result = clientGemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config={"task_type" : taskType}
    )
    return result.embeddings[0].values

def saveChunks(chunks, docName):
    for i, chunk in enumerate(chunks):
        embedding = generateEmbedding(chunk, taskType="RETRIEVAL_DOCUMENT")
        uniqueID = f"{docName}_chunk_{i}"
        collection.add(
            ids=[uniqueID],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"funete": docName}]
        )