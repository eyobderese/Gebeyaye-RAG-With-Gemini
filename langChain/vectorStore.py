from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_vectorstore(docs):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)

    return vectorstore


def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
