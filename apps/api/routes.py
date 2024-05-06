from flask_restx import Api, Resource, fields
from apps.api import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound

api = Api(blueprint)


@api.route("/graphdata")
class GraphData(Resource):
    def get(self):
        data = [3, 66, 41, -10, 25, 44, 9, 54]

        return jsonify(data)
