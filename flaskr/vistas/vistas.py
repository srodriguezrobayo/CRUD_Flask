from flask_restful import Resource
from ..modelos import db, Empleados, ReservacionSchema, lugar_reservacion, lugar_reservacionschema
#from ..modelos import Usuario, UsuarioSchema
from flask import request
from..modelos import Empleados,lugar_reservacion,Empleadosschema,lugar_reservacionschema

Empleados_schema = Empleadosschema()
lugar_reservacion_schema = lugar_reservacionschema()

class VistaEmpleados(Resource):
    def get(self):
        global Empleados
        return [Empleados_schema.dump(Empleados) for Empleados in Empleados.query.all()]

    def post(self):
        nuevo_Empleado = Empleados(nombre_Empleado=request.json['nombre_Empleado'],nom_empleado=request.json['nom_empleado'],correo_elec_admin=request.json['correo_elec_admin'],password_empleado=request.json['password_empleado'],tipo_usuario_idtipo_usuario=request.json['tipo_usuario_idtipo_usuario'],telefono_empleado=request.json['telefono_empleado'],genero_idgenero=request.json['genero_idgnero'])
        db.session.add(nuevo_Empleado)
        db.session.commit()
        return Empleados_schema.dump(nuevo_Empleado)

class VistaEmpleado(Resource):
    def get(self, id_Empleados):
        return Empleados_schema.dump(Empleados.query.get_or_404(id_Empleados))

    #actualizar
    def put(self, id_Empleados):
        Empleados = Empleados_schema.query.get_or_404(id_Empleados)
        Empleados.id_Empleado = request.json.get
        Empleados.nombre_Empleado = request.json.get
        db.session.commit()
        return Empleados_schema.dump(Empleados)

    def delete(self, id_Empleados):
        Empleado = Empleados.query.get_or_404(id_Empleados)
        db.session.delete(Empleado)
        db.session.commit()
        return 'Operacion exitosa', 204

class Vistalugares_reservaciones(Resource):
    def get(self):
        return [lugar_reservacion_schema.dump(lugar_reservacion) for lugar_reservacion in lugar_reservacion.query.all()]

    def post(self):
        nueva_lugar_reservacion = lugar_reservacion(nom_lugreserv=request.json['nom_lugreserv'],
                                        ciudad_id_ciudad=request.json['ciudad_id_ciudad'])
        db.session.add(nueva_lugar_reservacion)
        db.session.commit()
        return lugar_reservacion_schema.dump(nueva_lugar_reservacion)

class Vistalugar_reservacion(Resource):
    def get(self, id_lugar_reservacion):
        return lugar_reservacion_schema.dump(lugar_reservacion.query.get_or_404(id_lugar_reservacion))

    #actualizar
    def put(self, id_lugar_reservacion):
        lugar_reservacion = lugar_reservacion.query.get_or_404(id_lugar_reservacion)
        lugar_reservacion.id_direccion_lugreserv = request.json.get
        lugar_reservacion.nom_lugreserv = request.json.get
        lugar_reservacion.ciudad_id_ciudad = request.json.get
        db.session.commit()
        return Empleados_schema.dump(lugar_reservacion)

    def delete(self, id_lugar_reservacion):
        lugar_reservacion = lugar_reservacion.query.get_or_404(id_lugar_reservacion)
        db.session.delete(lugar_reservacion)
        db.session.commit()
        return 'Operacion exitosa', 204