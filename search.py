from database import clientGemini, clientChroma, collection, generateEmbedding

def searchRelevantChunk(question, n_results=4):
    embeddingQuestion= generateEmbedding(question, taskType="RETRIEVAL_QUERY")
    n_results= collection.query(
        query_embeddings=[embeddingQuestion],
        n_results= n_results
    )
    return n_results["documents"][0]

def answerQuestion(question):
    relevantChunks = searchRelevantChunk(question)
    context = "\n\n---\n\n".join(relevantChunks)
    prompt = f"""Sos un asistente de estudio. Respondé la pregunta del usuario
basándote ÚNICAMENTE en el siguiente contexto extraído de sus apuntes.
Si la respuesta no está en el contexto, decí que no encontraste esa
información en los documentos, no inventes nada.

CONTEXTO:
{context}

PREGUNTA:
{question}

RESPUESTA:"""
    answer = clientGemini.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return answer.text, relevantChunks