from flask import Flask, request, jsonify
import os
import pickle
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
import pandas as pd
import sqlite3


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

#1
@app.route('/v1/predict', methods=['GET'])
def predict():
    model = pickle.load(open('data/advertising_model','rb'))

    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)


    if tv is None or radio is None or newspaper is None:
        return "Missing args, the input values are needed to predict"
    else:
        prediction = model.predict([[int(tv), int(radio), int(newspaper)]])
        return "The prediction of sales investing that amount of money in TV, radio and newspaper is: " + str(round(prediction[0],2)) + 'k €'

#2
@app.route('/v2/ingest_data', methods=['POST'])
def ingest_data():

    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)
    sales = request.args.get('sales')

    connection = sqlite3.connect('data/advertising.db')
    cursor = connection.cursor()

    query = '''INSERT INTO campañas VALUES (?, ?, ?, ?)'''
    filters = [tv, radio, newspaper, sales]

    cursor.execute(query, filters)

    result = cursor.execute('''SELECT * FROM campañas''').fetchall()
    
    connection.commit()
    connection.close()

    return result


#3
@app.route('/v2/retrain', methods=['PUT'])
def retrain():
    connection = sqlite3.connect('data/advertising.db')
    cursor = connection.cursor()

    query = '''SELECT * FROM campañas'''
    result = cursor.execute(query).fetchall()
    

    df = pd.DataFrame(data = result, columns = ['tv', 'radio', 'newspaper', 'sales'])
    df = df.dropna()
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    model = pickle.load(open('data/advertising_model', 'rb'))

    mae_model = abs(cross_val_score(model, X, Y, scoring= 'neg_mean_absolute_error', cv = 5).mean())

    xgb_reg = XGBRegressor()
    xgb_reg.fit(X, Y)

    mae_new_model = abs(cross_val_score(xgb_reg, X, Y, scoring= 'neg_mean_absolute_error', cv = 5).mean())
    
    connection.close()

    if mae_model > mae_new_model:
        pickle.dump(xgb_reg, open('data/advertising_model', 'wb'))
        return f'Your model was updated, old mae: {mae_model}, new mae: {mae_new_model}'
    
    else:
        return f'Your old model is better, old mae: {mae_model}, new mae: {mae_new_model}'

app.run()

