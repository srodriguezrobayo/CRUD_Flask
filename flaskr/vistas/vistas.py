from flask_restful import Resource
from ..modelos import db, Servicio, ServicioSchema, Reservacion, ReservacionSchema
from ..modelos import TipoUsuario, TipoUsuarioSchema, Empresa, EmpresaSchema
from ..modelos import Departamento, Ciudad, DepartamentoSchema, CiudadSchema
from ..modelos import Genero, GeneroSchema, Cliente, ClienteSchema
from ..modelos import Empleados, Lugar_reservacion, EmpleadosSchema, Lugar_reservacionSchema
from flask import request

servicio_schema = ServicioSchema()
reservacion_schema = ReservacionSchema()
tipo_usuario_schema = TipoUsuarioSchema()
empresa_schema = EmpresaSchema()
departamento_schema = DepartamentoSchema()
ciudad_schema = CiudadSchema()
genero_schema = GeneroSchema()
cliente_schema = ClienteSchema()
empleados_schema = EmpleadosSchema()
lugar_reservacion_schema = Lugar_reservacionSchema()

class VistaEmpleados(Resource):
    def get(self):
        global Empleados
        return [empleados_schema.dump(Empleados) for Empleados in Empleados.query.all()]

    def post(self):
        nuevo_Empleado = Empleados(nombre_Empleado=request.json['nombre_Empleado'],nom_empleado=request.json['nom_empleado'],correo_elec_admin=request.json['correo_elec_admin'],password_empleado=request.json['password_empleado'],tipo_usuario_idtipo_usuario=request.json['tipo_usuario_idtipo_usuario'],telefono_empleado=request.json['telefono_empleado'],genero_idgenero=request.json['genero_idgnero'])
        db.session.add(nuevo_Empleado)
        db.session.commit()
        return empleados_schema.dump(nuevo_Empleado)

class VistaEmpleado(Resource):
    def get(self, id_Empleados):
        return empleados_schema.dump(Empleados.query.get_or_404(id_Empleados))

    #actualizar
    def put(self, id_Empleados):
        Empleados = empleados_schema.query.get_or_404(id_Empleados)
        Empleados.id_Empleado = request.json.get
        Empleados.nombre_Empleado = request.json.get
        db.session.commit()
        return empleados_schema.dump(Empleados)

    def delete(self, id_Empleados):
        Empleado = Empleados.query.get_or_404(id_Empleados)
        db.session.delete(Empleado)
        db.session.commit()
        return 'Operacion exitosa', 204

class Vistalugares_reservaciones(Resource):
    def get(self):
        return [lugar_reservacion_schema.dump(lugar_reservacion) for lugar_reservacion in Lugar_reservacion.query.all()]

    def post(self):
        nuevo_lugar_reservacion = Lugar_reservacion(nom_lugreserv=request.json['nom_lugreserv'],
                                        ciudad_id_ciudad=request.json['ciudad_id_ciudad'])
        db.session.add(nuevo_lugar_reservacion)
        db.session.commit()
        return lugar_reservacion_schema.dump(nuevo_lugar_reservacion)

class Vistalugar_reservacion(Resource):
    def get(self, id_lugar_reservacion):
        return lugar_reservacion_schema.dump(Lugar_reservacion.query.get_or_404(id_lugar_reservacion))

    #actualizar
    def put(self, id_lugar_reservacion):
        lugar_reservacion = Lugar_reservacion.query.get_or_404(id_lugar_reservacion)
        lugar_reservacion.id_direccion_lugreserv = request.json.get
        lugar_reservacion.nom_lugreserv = request.json.get
        lugar_reservacion.ciudad_id_ciudad = request.json.get
        db.session.commit()
        return lugar_reservacion_schema.dump(lugar_reservacion)

    def delete(self, id_lugar_reservacion):
        lugar_reservacion = Lugar_reservacion.query.get_or_404(id_lugar_reservacion)
        db.session.delete(lugar_reservacion)
        db.session.commit()
        return 'Operacion exitosa', 204

class VistaServicios(Resource):
    def get(self):
        return [servicio_schema.dump(Servicio) for Servicio in Servicio.query.all()]

    def post(self):
        nuevo_servicio = Servicio(nombre_servicio=request.json['nombre_servicio'])
        db.session.add(nuevo_servicio)
        db.session.commit()
        return servicio_schema.dump(nuevo_servicio)

class VistaServicio(Resource):
    def get(self, id_servicio):
        return servicio_schema.dump(Servicio.query.get_or_404(id_servicio))

    #actualizar
    def put(self, id_servicio):
        servicio = Servicio.query.get_or_404(id_servicio)
        servicio.id_servicio = request.json.get('id_servicio', servicio.id_servicio)
        servicio.nombre_servicio = request.json.get('nombre_servicio',servicio.nombre_servicio)
        db.session.commit()
        return servicio_schema.dump(servicio)

    def delete(self, id_servicio):
        servicio = Servicio.query.get_or_404(id_servicio)
        db.session.delete(servicio)
        db.session.commit()
        return 'Operacion exitosa', 204

class VistaReservaciones(Resource):
    def get(self):
        return [reservacion_schema.dump(Reservacion) for Reservacion in Reservacion.query.all()]

    def post(self):
        nueva_reservacion = Reservacion(servicio=request.json['servicio'],
                                        fecha_reservacion=request.json['fecha_reservacion'],
                                        hora_reservacion=request.json['hora_reservacion'],
                                        lugar_reservacion=request.json['lugar_reservacion'],
                                        empresa=request.json['empresa'],
                                        cliente=request.json['cliente'],
                                        valor=request.json['valor'],
                                        empleado=request.json['empleado'])
        db.session.add(nueva_reservacion)
        db.session.commit()
        return reservacion_schema.dump(nueva_reservacion)

class VistaReservacion(Resource):
    def get(self, id_reservacion):
        return reservacion_schema.dump(Reservacion.query.get_or_404(id_reservacion))

    #actualizar
    def put(self, id_reservacion):
        reservacion = Reservacion.query.get_or_404(id_reservacion)
        reservacion.id_reservacion = request.json.get('id_reservacion', reservacion.id_reservacion)
        reservacion.servicio = request.json.get('servicio',reservacion.servicio)
        reservacion.fecha_reservacion = request.json.get('fecha_reservacion',reservacion.fecha_reservacion)
        reservacion.hora_reservacion = request.json.get('hora_reseervacion',reservacion.hora_reservacion)
        reservacion.lugar_reservacion = request.json.get('lugar_reservacion',reservacion.lugar_reservacion)
        reservacion.empresa = request.json.get('empresa',reservacion.empresa)
        reservacion.cliente = request.json.get('cliente',reservacion.cliente)
        reservacion.valor = request.json.get('valor',reservacion.valor)
        reservacion.empleado = request.json.get('empleado',reservacion.empleado)
        db.session.commit()
        return servicio_schema.dump(reservacion)

    def delete(self, id_reservacion):
        reservacion = Reservacion.query.get_or_404(id_reservacion)
        db.session.delete(reservacion)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaTiposUsuarios(Resource):
    def get(self):
        return [tipo_usuario_schema.dump(TipoUsuario) for TipoUsuario in TipoUsuario.query.all()]

    def post(self):
        nuevo_tipo_usuario = TipoUsuario(idTipo_usuario=request.json['idTipo_usuario'], \
                                         Nombre_t_usuario=request.json['Nombre_t_usuario'], \
                                         estado=request.json['estado'])
        db.session.add(nuevo_tipo_usuario)
        db.session.commit()
        return tipo_usuario_schema.dump(nuevo_tipo_usuario)


class VistaTipoUsuario(Resource):
    def get(self, idTipo_usuario):
        return tipo_usuario_schema.dump(TipoUsuario.query.get_or_404(idTipo_usuario))

    def put(self, idTipo_usuario):
        tipo_usuario = TipoUsuario.query.get_or_404(idTipo_usuario)
        tipo_usuario.idTipo_usuario = request.json.get('idTipo_usuario', tipo_usuario.idTipo_usuario)
        tipo_usuario.Nombre_t_usuario = request.json.get('Nombre_t_usuario', tipo_usuario.Nombre_t_usuario)
        tipo_usuario.estado = request.json.get('estado', tipo_usuario.estado)
        db.session.commit()
        return tipo_usuario_schema.dump(tipo_usuario)

    def delete(self, idTipo_usuario):
        tipo_usuario = TipoUsuario.query.get_or_404(idTipo_usuario)
        db.session.delete(tipo_usuario)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaEmpresas(Resource):
    def get(self):
        return [empresa_schema.dump(Empresa) for Empresa in Empresa.query.all()]

    def post(self):
        nuevo_empresa = Empresa(Nit_empresa=request.json['Nit_empresa'], \
                                Nombre_empresa=request.json['Nombre_empresa'], \
                                Correoelectronico_empresa=request.json['Correoelectronico_empresa'], \
                                Password_empresa=request.json['Password_empresa'], \
                                Telefono_empresa=request.json['Telefono_empresa'], \
                                Ciudad_id_Ciudad=request.json['Ciudad_id_Ciudad'])
        db.session.add(nuevo_empresa)
        db.session.commit()
        return empresa_schema.dump(nuevo_empresa)


class VistaEmpresa(Resource):
    def get(self, Nit_empresa):
        return empresa_schema.dump(Empresa.query.get_or_404(Nit_empresa))

    def put(self, Nit_empresa):
        empresa = TipoUsuario.query.get_or_404(Nit_empresa)
        empresa.Nit_empresa = request.json.get('Nit_empresa', empresa.Nit_empresa)
        empresa.Nombre_empresa = request.json.get('Nombre_empresa', empresa.Nombre_empresa)
        empresa.Correoelectronico_empresa = request.json.get('Correoelectronico_empresa',
                                                             empresa.Correoelectronico_empresa)
        empresa.Password_empresa = request.json.get('Password_empresa', empresa.Password_empresa)
        empresa.Telefono_empresa = request.json.get('Telefono_empresa', empresa.Telefono_empresa)
        empresa.Ciudad_id_Ciudad = request.json.get('Ciudad_id_Ciudad', empresa.Ciudad_id_Ciudad)
        db.session.commit()
        return empresa_schema.dump(empresa)

    def delete(self, Nit_empresa):
        empresa = Empresa.query.get_or_404(Nit_empresa)
        db.session.delete(empresa)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaDepartamentos(Resource):
    def get(self):
        return [departamento_schema.dump(Departamento) for Departamento in Departamento.query.all()]

    def post(self):
        nuevo_departamento = Departamento(idDepartamento=request.json['idDepartamento'], )
        db.session.add(nuevo_departamento)
        db.session.commit()
        return departamento_schema.dump(nuevo_departamento)


class VistaDepartamento(Resource):
    def get(self, idDepartamento):
        return departamento_schema.dump(Departamento.query.get_or_404(idDepartamento))

    def put(self, idDepartamento):
        departamento = Departamento.query.get_or_404(idDepartamento)
        departamento.idDepartamento = request.json.get('idTipo_usuario', departamento.idDepartamento)
        db.session.commit()
        return departamento_schema.dump(departamento)

    def delete(self, idDepartamento):
        departamento = Departamento.query.get_or_404(idDepartamento)
        db.session.delete(departamento)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaCiudades(Resource):
    def get(self):
        return [ciudad_schema.dump(Ciudad) for Ciudad in Ciudad.query.all()]

    def post(self):
        nuevo_ciudad = Ciudad(id_Ciudad=request.json['id_Ciudad'])
        db.session.add(nuevo_ciudad)
        db.session.commit()
        return ciudad_schema.dump(nuevo_ciudad)


class VistaCiudad(Resource):
    def get(self, id_Ciudad):
        return ciudad_schema.dump(Ciudad.query.get_or_404(id_Ciudad))

    def put(self, id_Ciudad):
        ciudad = Ciudad.query.get_or_404(id_Ciudad)
        ciudad.id_Ciudad = request.json.get('id_Ciudad', Ciudad.id_Ciudad)
        db.session.commit()
        return ciudad_schema.dump(ciudad)

    def delete(self, id_Ciudad):
        ciudad = Ciudad.query.get_or_404(id_Ciudad)
        db.session.delete(ciudad)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaGeneros(Resource):
    def get(self):
        return [genero_schema.dump(Genero) for Genero in Genero.query.all()]

    def post(self):
        new_genero = Genero(idGenero=request.json['idGenero'], \
                            Desc_genero=request.json['Desc_genero'])
        db.session.add(new_genero)
        db.session.commit()
        return genero_schema.dump(new_genero)


class VistaGenero(Resource):
    def get(self, idGenero):
        return genero_schema.dump(Genero.query.get_or_404(idGenero))

    def put(self, idGenero):
        genero = Genero.query.get_or_404(idGenero)
        genero.idGenero = request.json.get('idGenero', genero.idGenero)
        genero.Desc_genero = request.json.get('Desc_genero', genero.Desc_genero)
        db.session.commit()
        return genero_schema.dump(genero)

    def delete(self, idGenero):
        genero = Genero.query.get_or_404(idGenero)
        db.session.delete(genero)
        db.session.commit()
        return 'Operacion exitosa', 204


class VistaClientes(Resource):
    def get(self):
        return [cliente_schema.dump(Cliente) for Cliente in Cliente.query.all()]

    def post(self):
        new_cliente = Cliente(id_Cliente=request.json['id_Cliente'], \
                              Nombre_cliente=request.json['Nombre_cliente'], \
                              Correoelectronico_cliente=request.json['Correoelectronico_cliente'], \
                              Password_cliente=request.json['Password_cliente'], \
                              Telefono_cliente=request.json['Telefono_cliente'], \
                              Genero_idGenero=request.json['Genero_idGenero'], \
                              Ciudad_id_Ciudad=request.json['Ciudad_id_Ciudad'])
        db.session.add(new_cliente)
        db.session.commit()
        return cliente_schema.dump(new_cliente)


class VistaCliente(Resource):
    def get(self, id_Cliente):
        return cliente_schema.dump(Cliente.query.get_or_404(id_Cliente))

    def put(self, id_Cliente):
        cliente = Genero.query.get_or_404(id_Cliente)
        cliente.id_Cliente = request.json.get('id_Cliente', cliente.id_Cliente)
        cliente.Nombre_cliente = request.json.get('Nombre_cliente', cliente.Nombre_cliente)
        cliente.Correoelectronico_cliente = request.json.get('Correoelectronico_cliente',
                                                             cliente.Correoelectronico_cliente)
        cliente.Password_cliente = request.json.get('Password_empresa', cliente.Password_cliente)
        cliente.Telefono_cliente = request.json.get('Telefono_empresa', cliente.Telefono_cliente)
        cliente.Genero_idGenero = request.json.get('Genero_idGenero', cliente.Genero_idGenero)
        cliente.Ciudad_id_Ciudad = request.json.get('Ciudad_id_Ciudad', cliente.Ciudad_id_Ciudad)
        db.session.commit()
        return cliente_schema.dump(cliente)

    def delete(self, id_Cliente):
        cliente = Cliente.query.get_or_404(id_Cliente)
        db.session.delete(cliente)
        db.session.commit()
        return 'Operacion exitosa', 204