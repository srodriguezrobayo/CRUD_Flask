from flask_restful import Resource
from ..modelos import db, Servicio, ServicioSchema
#from ..modelos import Album, AlbumSchema
#from ..modelos import Usuario, UsuarioSchema
from flask import request

servicio_schema = ServicioSchema()

class VistaServicios(Resource):
    def get(self):#Me trae todas las canciones
        return [servicio_schema.dump(Servicio) for Servicio in Servicio.query.all()]

    def post(self):
        nuevo_servicio = Servicio(nombre_servicio=request.json['nombre_servicio'])
        db.session.add(nuevo_servicio)#agrgar en la bd
        db.session.commit()#guardar los cambios
        return servicio_schema.dump(nuevo_servicio)#retornar la nueva cancion en formato json

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