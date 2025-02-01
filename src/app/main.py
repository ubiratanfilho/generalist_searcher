from utils.graph import graph
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_answer', methods=['POST'])
def generate_answer():
    data = request.get_json()
    question = data.get('question')
    thread_id = data.get('thread_id')
    
    if not question:
        return jsonify({"error": "Parâmetro 'question' não fornecido."}), 400

    config = {"configurable": {"thread_id": thread_id}}
    response = graph.invoke({"messages": [("user", question)], "question": question, "context": [], "web_search": False}, config)

    return jsonify({"message": response['messages'][-1].content})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)