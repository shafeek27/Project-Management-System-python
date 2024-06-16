from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

from routes import projects, tasks, teams, notifications
app.register_blueprint(projects.bp)
app.register_blueprint(tasks.bp)
app.register_blueprint(teams.bp)
app.register_blueprint(notifications.bp)

if __name__ == '__main__':
    app.run(debug=True)
