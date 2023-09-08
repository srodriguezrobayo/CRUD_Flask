from flaskr import create_app
from .modelos import db, Servicio, ServicioSchema, Reservacion, ReservacionSchema, TipoUsuario, TipoUsuarioSchema, Empresa, EmpresaSchema, Ciudad, CiudadSchema, Departamento, DepartamentoSchema, Genero, GeneroSchema, Cliente, ClienteSchema, Empleados, EmpleadosSchema, Lugar_reservacion, Lugar_reservacionSchema
from flask_restful import Api
from .vistas import VistaServicio, VistaServicios
from .vistas import VistaReservacion, VistaReservaciones
from .vistas import VistaEmpresa, VistaEmpresas
from .vistas import VistaTipoUsuario, VistaTiposUsuarios
from .vistas import VistaCiudad, VistaCiudades
from .vistas import VistaDepartamento, VistaDepartamentos
from .vistas import VistaGenero, VistaGeneros
from .vistas import VistaCliente, VistaClientes
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
api.add_resource(VistaServicios, '/servicios')
api.add_resource(VistaServicio, '/servicio/<int:id_servicio>')
api.add_resource(VistaReservaciones, '/reservaciones')
api.add_resource(VistaReservacion, '/reservacion/<int:id_reservacion>')
api.add_resource(VistaTipoUsuario, '/tipo_usuario/<int:idTipo_usuario>')
api.add_resource(VistaTiposUsuarios, '/tipos_usuarios')
api.add_resource(VistaEmpresa, '/empresa/<int:Nit_empresa>')
api.add_resource(VistaEmpresas, '/empresas')
api.add_resource(VistaCiudad, '/ciudad/<string:id_Ciudad>')
api.add_resource(VistaCiudades, '/ciudades')
api.add_resource(VistaDepartamento, '/departamento/<string:idDepartamento>')
api.add_resource(VistaDepartamentos, '/departamentos')
api.add_resource(VistaGenero, '/genero/<int:idGenero>')
api.add_resource(VistaGeneros, '/generos')
api.add_resource(VistaCliente, '/cliente/<int:id_Cliente>')
api.add_resource(VistaClientes, '/clientes')
api.add_resource(VistaEmpleado, '/empleado/<int:id_Empleados>')
api.add_resource(VistaEmpleados, '/empleados')
api.add_resource(Vistalugar_reservacion, '/lugar_reservacion/<int:id_lugar_reservacion>')
api.add_resource(Vistalugares_reservaciones, '/lugares_reservaciones')