'''
    @author: Edison Bejarano Garces
    @since: 06/09/2019
    @summary: Archivo principal:
'''
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from configuracion import conexion
import configuracion

app = Flask(__name__)
app.config["MONGO_URI"] = configuracion.SQLALCHEMY_DATABASE_URI
con = conexion().get_conection(app)
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],supports_credentials=True)

if __name__ == "__main__":
      from app import api_bp
      app.register_blueprint(api_bp, url_prefix='/api')
      app.run(debug=True,host= 'localhost')
