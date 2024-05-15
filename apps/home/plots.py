# import plotly
# import plotly.graph_objs as go
# import plotly.express as px
#
#
# import pandas as pd
# import numpy as np
# import json
# from ..connections.beatstream_connection import BeatstreamConnection, User, Recommendation
# from ..connections.million_connection import MillionConnection, Track
#
# class PlotCreator():
#     def __init__(self):
#         self.beat_connection = BeatstreamConnection()
#         self.million_connection = MillionConnection()
#
#     def create_total_model_score_chart(self):
#         beat_session = self.beat_connection.new_session()
#         data = {
#             "Predictive Models": [],
#             "Cumulative Score": []
#         }
#         for row in beat_session.query(Recommendation.modelID).distinct().all():
#             modelID = row[0]
#             data["Predictive Models"].append(f"Model #{modelID}")
#             total_score = 0
#             scores = beat_session.query(Recommendation.model_score).filter(Recommendation.modelID == modelID).all()
#             for score_row in scores:
#                 score = score_row[0]
#                 total_score += score
#             data["Cumulative Score"].append(total_score)
#         df = pd.DataFrame.from_dict(data)
#
#         data = [
#             go.Bar(
#                 x=df['Predictive Models'],
#                 y=df['Cumulative Score']
#             )
#         ]
#
#         graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
#         return graphJSON
#
