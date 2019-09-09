'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Clase para administracion de alumnos
'''
from imports import *
class Alumnos(Resource):
    def get(self):
        alumnos = con.db.alumnos
        datos = alumnos.find_one()
        output =  { 'prmr_nmbre'        :  datos['prmr_nmbre'],
                    'sgndo_nmbre'       :  datos['sgndo_nmbre'],
                    'prmr_aplldo'       :  datos['prmr_aplldo'],
                    'sgndo_aplldo'      :  datos['sgndo_aplldo'],
                    'nmro_idntfccn'     :  datos['nmro_idntfccn'],
                    'tpo_idntfccn'      :  datos['tpo_idntfccn'],
                    'gnro'              :  datos['gnro'],
                    'fcha_ncmnto'       :  datos['fcha_ncmnto'],
                    'tlfno_fjo'         :  datos['tlfno_fjo'],
                    'tlfno_cllr'        :  datos['tlfno_cllr'],
                    'drccn'             :  datos['drccn'],
                    'crr_elctrnco'      :  datos['crr_elctrnco']
                    }
        return jsonify({'Data':output})

    def put(self ,nmro_idntfccn):
        alumnos = con.db.alumnos



    def post(self):
           prmr_nmbre         =   request.form['prmr_nmbre'],
           sgndo_nmbre        =   request.form['sgndo_nmbre'],
           prmr_aplldo        =   request.form['prmr_aplldo'],
           sgndo_aplldo       =   request.form['sgndo_aplldo'],
           nmro_idntfccn      =   request.form['nmro_idntfccn'],
           tpo_idntfccn       =   request.form['tpo_idntfccn'],
           gnro               =   request.form['gnro'],
           fcha_ncmnto        =   request.form['fcha_ncmnto'],
           tlfno_fjo          =   request.form['tlfno_fjo'],
           tlfno_cllr         =   request.form['tlfno_cllr'],
           drccn              =   request.form['drccn'],
           crr_elctrnco       =   request.form['crr_elctrnco']
           alumnos = con.db.alumnos
           #inserto datos en la tabla alumnos
           alumnos_id = alumnos.insert({
                       'prmr_nmbre'        :  prmr_nmbre,
                       'sgndo_nmbre'       :  sgndo_nmbre,
                       'prmr_aplldo'       :  prmr_aplldo,
                       'sgndo_aplldo'      :  sgndo_aplldo,
                       'nmro_idntfccn'     :  nmro_idntfccn,
                       'tpo_idntfccn'      :  tpo_idntfccn,
                       'gnro'              :  gnro,
                       'fcha_ncmnto'       :  fcha_ncmnto,
                       'tlfno_fjo'         :  tlfno_fjo,
                       'tlfno_cllr'        :  tlfno_cllr,
                       'drccn'             :  drccn,
                       'crr_elctrnco'      :  crr_elctrnco
                       })
           #consulto datos
           datos = alumnos.find_one({'_id': alumnos_id})
           output =  { 'prmr_nmbre'        :  datos['prmr_nmbre'],
                       'sgndo_nmbre'       :  datos['sgndo_nmbre'],
                       'prmr_aplldo'       :  datos['prmr_aplldo'],
                       'sgndo_aplldo'      :  datos['sgndo_aplldo'],
                       'nmro_idntfccn'     :  datos['nmro_idntfccn'],
                       'tpo_idntfccn'      :  datos['tpo_idntfccn'],
                       'gnro'              :  datos['gnro'],
                       'fcha_ncmnto'       :  datos['fcha_ncmnto'],
                       'tlfno_fjo'         :  datos['tlfno_fjo'],
                       'tlfno_cllr'        :  datos['tlfno_cllr'],
                       'drccn'             :  datos['drccn'],
                       'crr_elctrnco'      :  datos['crr_elctrnco']
                       }
           return jsonify({'Data':output})
