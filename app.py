import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/api/winedata/<selections>")
def wine_recommendation(selections):
    
    connection = sqlite3.connect('flask_api/wine_database') 
    # connection.close()
    # Parse user selections from front end and find favored wine class
    selections_int = selections.split(",")
    selections_int = [int(selection) for selection in selections_int]
    selected_class = max(set(selections_int), key=selections_int.count)

    # Find new wine for recommendation
    # df = pd.read_csv('../Resources/wine_clean_clustered.csv')
    df = pd.read_sql(f"select name from wine_dataframe where class = {selected_class} order by random() limit 1 ",connection)
    df2 = pd.read_sql(f"select name from wine_dataframe where class = {selected_class} order by random() limit 1 ",connection)
    # df = df[df['class'] == selected_class]
    # df = df.sample(n=1)
    recommended_wine = str(df['name'].values[0])
    recommended_wine2 = str(df2['name'].values[0])
    connection.close()
    # Return new wine recommendation
    # return(recommended_wine)
    return jsonify({'Recommended 1':recommended_wine,
    'Recommended 2': recommended_wine2})

@app.route("/")
def home_page():
    """List all available api routes."""
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
