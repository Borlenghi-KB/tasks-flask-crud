from flask import Flask, request, jsonify
from models.task import Task  

app = Flask(__name__)

#CRUD - Create, Read, Update, Delete

task_list = [] 
task_id_control = 1

#POST____________________________________________________________________________

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() 
    global task_id_control
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_list.append(new_task)
    task_id_control += 1
    print(task_list)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

#GET____________________________________________________________________________

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_dict = [task.to_dict() for task in task_list]
    output = {
                "tasks": tasks_dict,
                "total_tasks": len(tasks_dict)
            }
    
    return jsonify(output)
    
#READ____________________________________________________________________________

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in task_list:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Tarefa não encontrada!"}), 404

#READ2____________________________________________________________________________

#@app.route('/user/<username>')
#def show_user(username):
#    print(username)
#   print(type(username))
#    return username


#UPADATE____________________________________________________________________________

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in task_list:
        if t.id == id:
            task = t
            break
    print(task)
    if task == None:
        return jsonify({"message": "Tarefa não encontrada!"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

#DELETE____________________________________________________________________________

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in task_list:
        if t.id == id:
            task = t
            break
    print(task)
    if task == None:
        return jsonify({"message": "Tarefa não encontrada!"}), 404

    task_list.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})


if __name__ == '__main__':  
    app.run(debug=True)  # Esse é o método que inicia a aplicação. Ele é utilizado para iniciar o servidor web e permitir que a aplicação seja acessada pelo navegador. O parâmetro debug=True é utilizado para habilitar o modo de depuração, que permite que a aplicação seja reiniciada automaticamente quando houver alterações no código.