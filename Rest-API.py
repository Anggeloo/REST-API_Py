from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Call the doctor", "completed": True},
]

# Route to get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Route to get a task by ID
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Route to create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.json
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route to update an existing task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        data = request.json
        task.update(data)
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Route to delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
