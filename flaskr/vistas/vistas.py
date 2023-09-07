from flask_restful import Resource
from ..modelos import db, Servicio, ServicioSchema, Reservacion, ReservacionSchema
#from ..modelos import Usuario, UsuarioSchema
from flask import request

servicio_schema = ServicioSchema()
reservacion_schema = ReservacionSchema

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
        reservacion.id_reservacion = request.json.get('id_reservacion', reservacion.id_servicio)
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