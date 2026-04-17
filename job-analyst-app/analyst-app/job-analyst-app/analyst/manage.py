import os
import unittest
import jwt
from dotenv import load_dotenv

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import request, session

from app.main.constant import paths
from app.main import create_app,db
from app import blueprint
from app.main.config.login_config import LoginConfig
login_obj = LoginConfig()
jwt_key = login_obj.get_jwt_key()

load_dotenv()
app = create_app(os.getenv('CURRENT_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    if paths.mode == "PROD":
        app.run(host='0.0.0.0', port=6007, use_reloader=False)
    elif paths.mode == "DEV":
        app.run(host='0.0.0.0', port=6008, use_reloader=False)
    else:
        app.run(host='0.0.0.0', port=5001, use_reloader=False)

@app.before_request
def read_header():
    if "authorization" in request.headers:
        bearer = request.headers["authorization"]
        token = bearer.replace("Bearer", "").strip()
        if token is not None and not token.startswith(" ") and token != "":
            header = jwt.get_unverified_header(token)
            decoded_jwt = jwt.decode(token, jwt_key, algorithms=header['alg'])
            session['loggedin'] = True
            session['designation'] = decoded_jwt["designation"]
            session['username'] = decoded_jwt["email"]

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
