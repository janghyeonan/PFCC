#Created by An Janghyun

from flask import Flask, request, abort
from flask_restx import Api, fields, Resource
import datetime
import pymysql

app = Flask(__name__)
api = Api(app)

task_model = api.model('Task', {
    'id': fields.String(required=True, description='Task ID'),
    'task': fields.String(required=True, description='Task description')
})

connet_user = {"abc" : "2023-01-01 00:00:00"}

# Connect to the MySQL database
connection = pymysql.connect(
    host='9.9.9.9',
    user='sa',
    password='psps',
    db='dn',
    charset='utf8',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
class TaskList(Resource):
    def get(self):
        cursor = connection.cursor()
        query = "SELECT id, task FROM tasks"
        cursor.execute(query)
        tasks = cursor.fetchall()
        return tasks, 200
    
    @api.expect(task_model)
    def post(self):
        cursor = connection.cursor()
        task = request.get_json()
        query = "INSERT INTO tasks (id, task) VALUES (%s, %s)"
        cursor.execute(query, (task["id"], task["task"]))
        connection.commit()
        return {"message": "Task created successfully"}, 201

class Task(Resource):
    def get(self, id):
        cursor = connection.cursor()
        query = "SELECT * FROM tasks WHERE id = %s"
        cursor.execute(query, (id,))
        task = cursor.fetchone()
        if task:
            return task, 200
        else:
            return {"message": "Task not found"}, 404
    
    @api.expect(task_model)
    def put(self, id):
        cursor = connection.cursor()
        task = request.get_json()
        query = "UPDATE tasks SET task = %s WHERE task_id = %s"
        cursor.execute(query, (task["task"], id))
        connection.commit()
        return {"message": "Task updated successfully"}, 200
    
    def delete(self, id):
        cursor = connection.cursor()
        query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        return {"message": "Task deleted successfully"}, 200

class Taskk(Resource):
    def get(self, id):
        #리스트에 추가하기전에 아이피가 있는지 검색
        #있다면, 기록에 남은 시간을 불러와서 현재 시간과 비교
        #시간이 너무 짧다면 비허용
        #우선은 바로 때렸을때 몇초인지 보자구
        print(connet_user)
        if request.remote_addr in connet_user:            
            diff = datetime.datetime.now() - connet_user[request.remote_addr] 
            print(diff.microseconds)
            connet_user[request.remote_addr] = datetime.datetime.now()
            if  diff.microseconds < 100000:
                print("입력이 너무 빠릅니다.")
                abort(403)  # Forbidden

            else:             
                cursor = connection.cursor()
                query = "SELECT id, task FROM tasks limit "+str(id*100) + ";"        
                cursor.execute(query)
                task = cursor.fetchall()        
                if task:
                    return task
                else:
                    return {"message": "Task not found"}, 404
        else:           
            connet_user[request.remote_addr] = datetime.datetime.now()
            cursor = connection.cursor()
            query = "SELECT id, task FROM tasks limit "+str(id*100) + ";"        
            cursor.execute(query)
            task = cursor.fetchall()        
            if task:
                return task
            else:
                return {"message": "Task not found"}, 404
                

api.add_resource(TaskList, "/tasks")
api.add_resource(Taskk, "/taskk/<int:id>")
api.add_resource(Task, "/tasks/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)