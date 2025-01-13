# Task Management REST API
This is a simple REST API developed in Python using the Flask framework. It allows to perform CRUD (Create, Read, Update and Delete) operations on a list of tasks.

## 📋 Requirements
Before running the project, make sure you have the following installed:

Python 3.7 or higher.
Pip: Usually comes pre-installed with Python.
Flask: Can be installed using pip.

## ⚙️ Installation
Clone this repository or download the source code:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd your_repository
```
Install the necessary dependencies:
```bash
pip install flask
```

## 🚀 Execute
Make sure you are in the directory where the main file (REST-API.py) is located.

Run the Flask server:

```bash
python REST-API.py
```
If everything is correct, you will see a message similar to this:
```csharp
Running on http://127.0.0.1:5000
```
Access the API from your browser or with tools like Postman or cURL.

## 🛠️ Endpoints
### 1. Get all tasks
**Description**: Returns a list of all tasks.
**Method**: GET
**URL**: /tasks
**Example response**:
```bash
[
    {“id”: 1, “title”: “Buy food”, “completed”: false},
    {“id”: 2, “title”: “Call doctor”, “completed”: true}
]
```
### 2. Get a task by ID
**Description**: Return a specific task according to its ID.
**Method**: GET
***URL**: /tasks/<id>
**Example response**:
```bash
{
    “id": 1,
    “title": ‘Buy food’,
    “completed": false
}
```
### 3. Create a new task
**Description**: Add a new task to the list.
**Method**: POST
**URL**: /tasks
**Body (JSON)**:
```bash
{
    “title": ‘New task’,
    “completed": false
}
```
### Example response:
```bash
{
    “id": 3,
    “title": ‘New task’,
    “completed": false
}
```
### 4. Update a task
**Description**: Update the data of a specific task.
**Method**: PUT
**URL**: /tasks/<id>
**Body (JSON)**:
```bash
{
    “title": ‘Task updated’,
    “completed": true
}
```
### Example response:
```bash
{
    “id": 1,
    “title": ‘Task updated’,
    “completed": true
}
```
### 5. Delete a task
**Description**: Deletes a specific task by its ID.
**Method**: DELETE
**URL**: /tasks/<id>
**Example response**:
```bash
{
    “message": ”Task deleted”
}
```
## 🧪 Pruebas con Postman

- Configure the following requests in Postman:
- GET /tasks
- POST /tasks with JSON body to create a new task.
- PUT /tasks/<id> with JSON body to update a task.
- DELETE /tasks/<id> to delete a task.
- Sends the requests and checks the responses.
