import numpy as np
import pandas as pd
# from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
# from sklearn.externals import joblib
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

engine = create_engine('postgresql://postgres:postgres@localhost:5432/wine_db')
connection = engine.connect()

app = Flask(__name__)
CORS(app)
# wine_model = joblib.load('wine.md1')

@app.route("/api/winedata/<selections>")
def wine_recommendation(selections):

    # Parse user selections from front end and find favored wine class
    selections_int = selections.split(",")
    selections_int = [int(selection) for selection in selections_int]
    selected_class = max(set(selections_int), key=selections_int.count)

    # Find new wine for recommendation
    # df = pd.read_csv('../Resources/wine_clean_clustered.csv')
    df = pd.read_sql(f"select * from wine_df",connection)
    df = df[df['class'] == selected_class]
    df = df.sample(n=1)
    recommended_wine = str(df['name'].values[0])

    # Return new wine recommendation
    # return(recommended_wine)
    return recommended_wine.to_json(orient="records")





# class Predict(Resource):

#     @statitcmethod
#     def post():
#         parser = reqparse.RequestParser()
#         parser.add_argument('')
#         parser.add_argument('')
#         parser.add_argument('')

#         args = parser.parse_args() 

#        wine_predicted = np.fromiter(args.values(), dtype=float)  # convert input to array

#         out = {'Prediction': wine_model.predict([wine_predicted])[0]}

#          return out, 200

# api.add_resource(Predict, '/')


# @app.route("/")
# def home_page():
#     """List all available api routes."""
#     return render_template('index.html', data=wine_model) #data = to put my prediction to pass a python variable 

#     response = jsonify(all_summary_view_list)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


if __name__ == '__main__':
    app.run(debug=True)
