from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from rag import (
    generate_text,
    process_query
)


app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["POST"])
@cross_origin()
def api_query():
    data = request.get_json()
    user_query = data.get("query")
    print(user_query)

    if not user_query:
        return jsonify({"error": "Query not provided"}), 400

    # Create RAG chain
    prompt = process_query(user_query)

    response = generate_text(prompt)
    print(response)

    # Get response from the chain

    # Return the response as JSON
    return jsonify({"query": user_query, "response": response})


if __name__ == "__main__":
    app.run(debug=True)
