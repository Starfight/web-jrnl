# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api, Resource, abort

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)


@api.resource("/")
class Journal(Resource):
    def get(self):
        abort(501)
