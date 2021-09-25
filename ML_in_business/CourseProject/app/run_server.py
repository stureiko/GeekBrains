#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask
from flask import Flask, jsonify
import numpy as np
import dill

dill._dill._reverse_typemap['ClassType'] = type
import pandas as pd

app = Flask(__name__)
model = None


def load_model(model_path):
    # load the pre-trained model
    global model
    with open(model_path, 'rb') as f:
        model = dill.load(f)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route("/", methods=["GET"])
def general():
    return "Welcome to prediction process"


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        description, company_profile, benefits = "", "", "qq"
        request_json = flask.request.get_json()
        if request_json["description"]:
            description = request_json['description']
        if request_json["company_profile"]:
            company_profile = request_json['company_profile']
        if request_json["benefits"]:
            benefits = request_json['benefits']

        preds = model.predict_proba(pd.DataFrame({"description": [description],
                                                  "company_profile": [company_profile],
                                                  "benefits": [benefits]}))
        data["predictions"] = preds[:, 1][0]
        data["description"] = description
        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


if __name__ == '__main__':
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    modelpath = './models/logreg_pipline.dill'
    load_model(modelpath)
    app.run(debug=True, host='0.0.0.0')
