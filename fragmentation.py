def sliptInChunks(text, sizeOfChunk = 800, overlap = 100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + sizeOfChunk
        chunk = text[start:end]
        chunks.append(chunk)
        start += sizeOfChunk - overlap
    return chunks