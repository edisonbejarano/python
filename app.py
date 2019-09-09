'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Declaracion de las Rutas
'''
from flask_restful                       import Api
from flask                               import Blueprint
from resource.Alumnos                    import Alumnos
from resource.Profesores                 import Profesores
from resource.Asignaturas                import Asignaturas

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Alumnos, '/Alumnos/',  methods=['PUT','GET','POST'])
api.add_resource(Profesores, '/Profesores/',  methods=['PUT','GET','POST'])
api.add_resource(Asignaturas, '/Asignaturas/<page>',  methods=['PUT','GET','POST'])
