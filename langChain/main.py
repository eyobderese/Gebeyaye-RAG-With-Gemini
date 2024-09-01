from chains import create_rag_chain


def main():
    # Assume `retriever` is defined elsewhere or passed in
    retriever = None  # Replace this with your retriever object

    # Create the RAG chain
    rag_chain = create_rag_chain(retriever)

    # Invoke the RAG chain with a question
    response = rag_chain.invoke({"input": "who is Eyob Derese"})

    # Print the response
    print(response["answer"])


if __name__ == "__main__":
    main()
