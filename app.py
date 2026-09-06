import streamlit as st
import tempfile
import os
from documents import extractText
from fragmentation import sliptInChunks
from database import saveChunks
from search import answerQuestion

st.set_page_config(page_title="RAG de estudio")
st.title("Asistente de estudio")

if "historial" not in st.session_state:
    st.session_state.historial = []

st.header("1. Subi tus apuntes")
uploadedFiles = st.file_uploader("PDF o Word", type=["pdf", "docx"])

if uploadedFiles is not None: 
    if st.button("Procesar documento"):
        with st.spinner("Extrayendo texto y generando embeddings..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploadedFiles.name}") as tmp:
                tmp.write(uploadedFiles.getvalue())
                tempRoute = tmp.name

            text = extractText(tempRoute)
            chunks = sliptInChunks(text)
            saveChunks(chunks, docName=uploadedFiles.name)

            os.remove(tempRoute)

        st.success(f"Documento procesado: {len(chunks)} fragmentos guardados.")

st.header("2. Hacé una pregunta")
question = st.text_input("¿Qué querés saber de tus apuntes?")

if st.button("Preguntar") and question:
    with st.spinner("Buscando en tus apuntes..."):
        answer, chunks_usados = answerQuestion(question)

    st.session_state.historial.append((question, answer, chunks_usados))

if st.session_state.historial:
    st.header("Historial")
    for p, r, chunks in reversed(st.session_state.historial):
        st.markdown(f"**Pregunta:** {p}")
        st.markdown(f"**Respuesta:** {r}")
        with st.expander("Ver fragmentos usados como fuente"):
            for c in chunks:
                st.text(c)
        st.divider()