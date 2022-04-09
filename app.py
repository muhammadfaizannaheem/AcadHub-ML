import pandas as pd
from flask import Flask, request,jsonify,render_template
import joblib
import numpy as np

app=Flask(__name__)

model=joblib.load('KNN Trained and Saved Model.sav')

# @app.route('/predicts',methods = ['POST','GET'])
# def predicts():
#     json = request.json
#     query_df=pd.DataFrame(json)
#     prediction = model.predict(query_df)
#     return jsonify({'Prediction ': list(prediction) })
@app.route('/predict',methods = ['POST'])
def ping():
    response.headers.add('Access-Control-Allow-Origin', '*')
    testtext=request.json
    query_df=pd.DataFrame(testtext)
    prediction = model.predict(query_df)
    return jsonify({'Prediction ': int(prediction) })

if __name__ == '__main__':
    app.run(debug=True)
