from flaskr import create_app
from flask_restful import Api
from flask_migrate import Migrate
from .modelos import db
from .vistas import VistaDepartamento, VistaDepartamentos, VistaCiudad, VistaCiudades

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

migrate = Migrate()
migrate.init_app(app, db, compare_type=True)
api = Api(app)

api.add_resource(VistaDepartamento, '/departamento')
api.add_resource(VistaDepartamentos, '/departamentos')
api.add_resource(VistaCiudad, '/ciudad')
api.add_resource(VistaCiudades, '/ciudades')