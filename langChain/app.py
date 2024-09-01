from flask import Flask, request, jsonify, render_template
from loader import load_and_chunk_pdf
from vectorStore import create_vectorstore, get_retriever
from chains import create_rag_chain
import config

app = Flask(__name__)

# Load and prepare documents
docs = load_and_chunk_pdf(
    '../context_Document/document.pdf')

# Create vector store and retriever
vectorstore = create_vectorstore(docs)
retriever = get_retriever(vectorstore)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]

        # Create RAG chain
        rag_chain = create_rag_chain(retriever)

        # Get response from the chain
        response = rag_chain.invoke({"input": user_query})

        # Return the response
        return render_template("index.html", query=user_query, response=response["answer"])

    return render_template("index.html")


@app.route("/api/query", methods=["POST"])
def api_query():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query not provided"}), 400

    # Create RAG chain
    rag_chain = create_rag_chain(retriever)

    # Get response from the chain
    response = rag_chain.invoke({"input": user_query})

    # Return the response as JSON
    return jsonify({"query": user_query, "response": response["answer"]})


if __name__ == "__main__":
    app.run(debug=True)
