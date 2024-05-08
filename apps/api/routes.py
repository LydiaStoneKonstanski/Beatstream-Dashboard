from flask_restx import Api, Resource, fields
from sqlalchemy import func

from apps.api import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from ..connections.beatstream_connection import BeatstreamConnection, User, Recommendation

api = Api(blueprint)

beatstream_connection = BeatstreamConnection()
beatstream_session = beatstream_connection.new_session()


@api.route("/graphdata")
class GraphData(Resource):
    def get(self):
        data = [3, 66, 41, -10, 25, 44, 9, 54]

        return jsonify(data)

@api.route("/modelscores")
class ModelScores(Resource):
    def get(self):

        results = beatstream_session.query(Recommendation.modelID, func.sum(Recommendation.model_score)
                                           ).group_by(Recommendation.modelID).all()

        model_scores = {}
        for result in results:
            model_scores[result[0]] = float(result[1])

        series = [
            {
                'name': "Males",
                'data': [x for x in model_scores.values()]
            },
            {
                'name': "Females",
                'data': [x for x in model_scores.values()]
            },
        ]

        data = {
            'series': series,
            'categories': list(model_scores.keys())
        }
        return jsonify(data)
