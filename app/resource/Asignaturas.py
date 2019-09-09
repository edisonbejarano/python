'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Clase para administracion de alumnos
'''
from imports import *
class Asignaturas(Resource):
    def get(self):
        asignaturas = con.db.asignaturas
        datos = asignaturas.find_one()
        output =  { 'cdgo'        :  datos['cdgo'],
                    'dscrpcn'     :  datos['dscrpcn'],
                    'rqsts'       :  datos['rqsts']
                    }
        return jsonify({'Data':output})

    def put(self ,cdgo):
        #asignaturas = con.db.asignaturas
        cdgo    = request.form['cdgo']
        dscrpcn = request.form['dscrpcn']
        rqsts   = request.form['rqsts']
        print(cdgo)
        #asignaturas = asignaturas.update_one({"cdgo": cdgo},{"$set": {"dscrpcn" : dscrpcn,"rqsts" : rqsts}})


    def post(self):
           cdgo         =   request.form['cdgo'],
           dscrpcn      =   request.form['dscrpcn'],
           rqsts        =   request.form['rqsts']
           asignaturas = con.db.asignaturas
           #inserto datos en la tabla Asignaturas
           asignaturas_id = asignaturas.insert({
                       'cdgo'        :  cdgo,
                       'dscrpcn'     :  dscrpcn,
                       'rqsts'       :  rqsts
                       })
           #consulto datos
           datos = asignaturas.find_one({'_id': asignaturas_id})
           output =  { 'cdgo'        :  datos['cdgo'],
                       'dscrpcn'     :  datos['dscrpcn'],
                       'rqsts'       :  datos['rqsts']
                       }
           return jsonify({'Data':output})
