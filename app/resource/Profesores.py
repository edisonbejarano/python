'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Clase para administracion de profesores
'''
from imports import *
class Profesores(Resource):
    def get(self):
        profesores = con.db.profesores
        datos = profesores.find_one()
        output =  { 'prmr_nmbre'        :  datos['prmr_nmbre'],
                    'sgndo_nmbre'       :  datos['sgndo_nmbre'],
                    'prmr_aplldo'       :  datos['prmr_aplldo'],
                    'sgndo_aplldo'      :  datos['sgndo_aplldo'],
                    'nmro_idntfccn'     :  datos['nmro_idntfccn'],
                    'tpo_idntfccn'      :  datos['tpo_idntfccn'],
                    'tlfno_cllr'        :  datos['tlfno_cllr'],
                    'crr_elctrnco'      :  datos['crr_elctrnco']
                    }
        return jsonify({'Data':output})

    def put(self ,nmro_idntfccn):
        profesores = con.db.profesores



    def post(self):
           prmr_nmbre         =   request.form['prmr_nmbre'],
           sgndo_nmbre        =   request.form['sgndo_nmbre'],
           prmr_aplldo        =   request.form['prmr_aplldo'],
           sgndo_aplldo       =   request.form['sgndo_aplldo'],
           nmro_idntfccn      =   request.form['nmro_idntfccn'],
           tpo_idntfccn       =   request.form['tpo_idntfccn'],
           tlfno_cllr         =   request.form['tlfno_cllr'],
           crr_elctrnco       =   request.form['crr_elctrnco']
           profesores = con.db.profesores
           #inserto datos en la tabla profesores
           profesores_id = profesores.insert({
                       'prmr_nmbre'        :  prmr_nmbre,
                       'sgndo_nmbre'       :  sgndo_nmbre,
                       'prmr_aplldo'       :  prmr_aplldo,
                       'sgndo_aplldo'      :  sgndo_aplldo,
                       'nmro_idntfccn'     :  nmro_idntfccn,
                       'tpo_idntfccn'      :  tpo_idntfccn,
                       'tlfno_cllr'        :  tlfno_cllr,
                       'crr_elctrnco'      :  crr_elctrnco
                       })
           #consulto datos
           datos = profesores.find_one({'_id': profesores_id})
           output =  { 'prmr_nmbre'        :  datos['prmr_nmbre'],
                       'sgndo_nmbre'       :  datos['sgndo_nmbre'],
                       'prmr_aplldo'       :  datos['prmr_aplldo'],
                       'sgndo_aplldo'      :  datos['sgndo_aplldo'],
                       'nmro_idntfccn'     :  datos['nmro_idntfccn'],
                       'tpo_idntfccn'      :  datos['tpo_idntfccn'],
                       'tlfno_cllr'        :  datos['tlfno_cllr'],
                       'crr_elctrnco'      :  datos['crr_elctrnco']
                       }
           return jsonify({'Data':output})
