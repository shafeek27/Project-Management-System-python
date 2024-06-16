from flask import Blueprint, request, jsonify
from app import db
from models import Task
from schemas import TaskSchema

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    task_schema = TaskSchema()
    task = task_schema.load(data)
    db.session.add(task)
    db.session.commit()
    return task_schema.jsonify(task)

@bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_schema = TaskSchema(many=True)
    return task_schema.jsonify(tasks)

# Additional endpoints for update and delete can be added similarly
