from flask import Blueprint, request, jsonify
from app import db
from models import Project
from schemas import ProjectSchema

bp = Blueprint('projects', __name__, url_prefix='/projects')

@bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    project_schema = ProjectSchema()
    project = project_schema.load(data)
    db.session.add(project)
    db.session.commit()
    return project_schema.jsonify(project)

@bp.route('/', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    project_schema = ProjectSchema(many=True)
    return project_schema.jsonify(projects)

# Additional endpoints for update and delete can be added similarly
