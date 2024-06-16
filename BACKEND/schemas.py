from app import ma
from models import User, Project, Team, Task, Notification

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

class NotificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notification
