from text_processing import load_data, chunk_text
from utils import load_embedded_data, save_embedded_data
from text_processing import chunk_text
import google.generativeai as genai
import numpy as np

Gapi_key = 'AIzaSyDOFJ0_MKoCK4qAfiyFGTXDjKXrZhIH2e4'


def embed_chunks(chunks):
    genai.configure(api_key=Gapi_key)
    embeddings = []
    for chunk in chunks:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=chunk,
            task_type="retrieval_document")

        embeddings.append(result)
    return embeddings


def calculate_similarity(embedded_data, embedded_query):
    query_embedding = np.array(embedded_query["embedding"])

    similarity_array = []
    for embedding in embedded_data:
        # Convert embedding to a NumPy array
        embedding_array = np.array(embedding["embedding"])
        # Calculate cosine similarity
        similarity = np.dot(query_embedding, embedding_array) / \
            (np.linalg.norm(query_embedding) * np.linalg.norm(embedding_array))
        similarity_array.append(similarity)
    return similarity_array


def get_top_n_chunks(chunks, similarity_array, n=10):
    zipped = zip(chunks, similarity_array)
    sorted_chunks = sorted(zipped, key=lambda x: x[1], reverse=True)
    top_n_chunks = [chunk for chunk, similarity in sorted_chunks[:n]]
    return top_n_chunks


def create_context(top_chunks):
    context = " ".join(top_chunks)
    return context


def generate_text(prompt):
    response = genai.generate_text(
        model='models/text-bison-001',  # You can explore other models as well
        prompt=prompt,
        temperature=0.7,  # Adjust as needed
        max_output_tokens=1024  # Adjust as needed
    )
    return response.result


def process_query(query):
    embedded_data_path = './embedded_date.pkl'
    text = load_data()
    chunks = chunk_text(text)

    try:
        # Try to load the embedded data
        embedded_data = load_embedded_data(embedded_data_path)
    except FileNotFoundError:
        # If the file is not found, load and chunk the text

        # Embed the chunks and save the embedded data
        embedded_data = embed_chunks(chunks)
        save_embedded_data(embedded_data_path, embedded_data)

        # Re-fetch the embedded data
        embedded_data = load_embedded_data(embedded_data_path)

    # Chunk and embed the query
    chunked_query = chunk_text(query)
    embedded_query = embed_chunks(chunked_query)

    # Calculate similarity and retrieve relevant chunks
    similarity_array = calculate_similarity(embedded_data, embedded_query[0])
    top_chunks = get_top_n_chunks(chunks, similarity_array, n=10)

    # Create context and generate response
    context = create_context(top_chunks)
    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

    return prompt
