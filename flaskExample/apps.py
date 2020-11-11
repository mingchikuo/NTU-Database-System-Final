import os
from flask import Flask
from flask_restful import Api
import logging
import sys
from params import params
from src.service.memberService.controller.signup import Singup
sys.dont_write_bytecode = True #disable __pycache__
param=params()
app = Flask(__name__)
api = Api(app)

api.add_resource(Singup,"/member/signup")

if __name__ == "__main__":
    if '--debug' in sys.argv:
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    else:
        logging.basicConfig(level=logging.INFO , format='[%(levelname)s] %(message)s')
    logging.info(f'Inanalysis running at port {param.port}')
    app.run(debug='--debug' in sys.argv,port=param.port,host=param.host)
