from flaskr import create_app
from flask_restful import Api
from flask_migrate import Migrate
from .modelos import db
from .vistas import VistaTipoUsuario, VistaTiposUsuarios, VistaEmpresa, VistaEmpresas

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

migrate = Migrate()
migrate.init_app(app, db, compare_type=True)
api = Api(app)

api.add_resource(VistaTipoUsuario, '/tipo_usuario')
api.add_resource(VistaTiposUsuarios, '/tipos_usuarios')
api.add_resource(VistaEmpresa, '/empresa')
api.add_resource(VistaEmpresas, '/empresas')