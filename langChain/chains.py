from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from prompts import get_prompt_template

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro", temperature=0.3, max_tokens=500)


def create_question_answer_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", temperature=0.3, max_tokens=500)
    prompt = get_prompt_template()
    return create_stuff_documents_chain(llm, prompt)


def create_rag_chain(retriever):
    question_answer_chain = create_question_answer_chain()
    return create_retrieval_chain(retriever, question_answer_chain)
