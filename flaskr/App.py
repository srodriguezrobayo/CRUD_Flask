from flaskr import create_app
from .modelos import db, Servicio, ServicioSchema
from flask_restful import Api
from .vistas import VistaServicio, VistaServicios
#from .vistas import VistaAlbumes, VistaAlbum
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


#with app.app_context():
    #Album_Schema = AlbumSchema()
    #A = Album(titulo='Prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #db.session.add(A)
    #db.session.commit()
    #print([Album_Schema.dumps(album) for album in Album.query.all()])

#with app.app_context():
    #u = Usuario(nombre='Juan', contrasenia='12345')
    #c = Cancion(titulo="prueba", minutos=2, segundos=25, interprete="Haaland")
    #a = Album(titulo='XD', anio=1999, descripcion='POP', medio=Medio.CD)
    #u.albumes.append(a)
    #a.canciones.append(c)
    #db.session.add(u)
    #db.session.add(c)
    #db.session.commit()
    #print(Album.query.all())
    #print(Album.query.all()[0].canciones)
    #db.session.delete(a)
    #print(Album.query.all())
    #print(Cancion.query.all())

#prueba

#with app.app_context():
    #u = Usuario(nombre='Juan', contrasena='12345')
    #a = Album(tiulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #u.albumes.append(a)
    #db.session.add(u)
    #db.session.commit()
    #print(Usuario.query.all())
    #print(Usuario.query.all()[0].albumes)
    #db.session.delete(u)
    #print(Usuario.query.all())
    #print(Album.query.all())