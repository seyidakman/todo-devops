from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
counter = 1

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    global counter
    data = request.get_json()
    todo = {
        "id": counter,
        "title": data.get("title"),
        "done": False
    }
    todos.append(todo)
    counter += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "silindi"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)