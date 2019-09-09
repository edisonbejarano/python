'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Archivo de configuracion a la BD:
'''
import os
from flask_pymongo import PyMongo

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mongodb://127.0.0.1:27017/proyecto"

class conexion():
    def get_conection(self,con):
        return PyMongo(con)
