import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.colors as mcolors
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Polygon
import os
import wget
import openpyxl
import math
class VizCreator():
    # def __init__(self):
    #     self.beat_connection = BeatstreamConnection()
    #     self.million_connection = MillionConnection()
    df = pd.read_excel(os.getcwd() + 'data/mapdata2021.xlsx', skiprows=4)
    df = df.rename(columns={'Unnamed: 0': 'state', 'Percent': 'pct_food_insecure'})
    df = df[['state', 'pct_food_insecure']]
    gdf = gpd.read_file('data/cb_2018_us_state_500k copy')
    gdf = gdf.merge(df, left_on='STUSPS', right_on='state')
    alask_gdf = gdf[gdf.state == 'AK']
    hawaii_gdf = gdf[gdf.state == 'HI']
    visframe = gdf.to_crs({'init': 'epsg:2163'})
    fig, ax = plt.subplots(1, figsize=(18, 14))

    ax.axis('off')
    visframe[~visframe.state.isin(['HI', 'AK'])].plot(color='lightblue', linewidth=0.8, ax=ax, edgecolor='0.8')

    akax = fig.add_axes([0.1, 0.17, 0.17, 0.16])

    hiax = fig.add_axes([.28, 0.20, 0.1, 0.1])