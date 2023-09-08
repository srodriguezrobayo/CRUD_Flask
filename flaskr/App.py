from flaskr import create_app
from .modelos import db, Empleados, Empleadosschema, lugar_reservacion, lugar_reservacionschema
from flask_restful import Api
from .vistas import VistaEmpleado, VistaEmpleados
from .vistas import Vistalugar_reservacion, Vistalugares_reservaciones
from flask_migrate import Migrate


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
migrate=Migrate()
migrate.init_app(app,db,compare_type=True)

api = Api(app)
api.add_resource(VistaEmpleado, '/Empleado/<int:id_Empleados')
api.add_resource(VistaEmpleados, '/Empleados')
api.add_resource(Vistalugar_reservacion, '/lugar_reservacion/<int:id_lugar_reservacion')
api.add_resource(Vistalugares_reservaciones, '/lugares_reservaciones')