from flaskr import create_app
from .modelos import db, Servicio, ServicioSchema, Reservacion, ReservacionSchema
from flask_restful import Api
from .vistas import VistaServicio, VistaServicios
from .vistas import VistaReservacion, VistaReservaciones
from flask_migrate import Migrate


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
migrate=Migrate()
migrate.init_app(app,db,compare_type=True)

api = Api(app)
api.add_resource(VistaServicios, '/servicios')
api.add_resource(VistaServicio, '/servicio/<int:id_servicio>')
api.add_resource(VistaReservaciones, '/reservaciones')
api.add_resource(VistaReservacion, '/reservacion/<int:id_reservacion>')