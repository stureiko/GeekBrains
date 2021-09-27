# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd
import os

dill._dill._reverse_typemap['ClassType'] = type
# import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

#
# def load_model(model_path):
#     # load the pre-trained model
#     global model
#     with open(model_path, 'rb') as f:
#         model = dill.load(f)
#     print(model)


def load_course_model(course_model_path):
    # load the pre-trained model
    global course_model
    with open(course_model_path, 'rb') as f:
        course_model = dill.load(f)
    print(course_model)


# modelpath = "app/models/logreg_pipeline.dill"
# # modelpath = "/app/models/logreg_pipeline.dill"
# load_model(modelpath)


course_model_path = "app/models/model_rand_for_reg.dill"
load_course_model(course_model_path)

@app.route("/", methods=["GET"])
def general():
    return """Welcome to fraudelent prediction process. Please use 'http://<address>/predict' to POST"""


# @app.route("/predict", methods=["POST"])
# def predict():
#     # initialize the data dictionary that will be returned from the
#     # view
#     data = {"success": False}
#     dt = strftime("[%Y-%b-%d %H:%M:%S]")
#     # ensure an image was properly uploaded to our endpoint
#     if flask.request.method == "POST":
#
#         description, company_profile, benefits = "", "", ""
#         request_json = flask.request.get_json()
#         if request_json["description"]:
#             description = request_json['description']
#
#         if request_json["company_profile"]:
#             company_profile = request_json['company_profile']
#
#         if request_json["benefits"]:
#             benefits = request_json['benefits']
#         logger.info(f'{dt} Data: description={description}, company_profile={company_profile}, benefits={benefits}')
#         try:
#             preds = model.predict_proba(pd.DataFrame({"description": [description],
#                                                       "company_profile": [company_profile],
#                                                       "benefits": [benefits]}))
#         except AttributeError as e:
#             logger.warning(f'{dt} Exception: {str(e)}')
#             data['predictions'] = str(e)
#             data['success'] = False
#             return flask.jsonify(data)
#
#         data["predictions"] = preds[:, 1][0]
#         # indicate that the request was a success
#         data["success"] = True
#
#     # return the data dictionary as a JSON response
#     return flask.jsonify(data)


global countries
countries = pd.read_csv('app/models/countries.csv')['0']

global provinces
provinces = pd.read_csv('app/models/provinces.csv')['0']


def get_request(r_l):
    r_df = pd.DataFrame(columns=['description', 'designation', 'price', 'region_1', 'variety', 'winery'])
    r_df.loc[len(r_df)] = [r_l['description'], r_l['designation'], r_l['price'], r_l['region_1'], r_l['variety'],
                           r_l['winery']]
    for c_name in countries:
        s = 'country_' + c_name
        if r_l['country'] == c_name:
            r_df[s] = 1
        else:
            r_df[s] = 0

    for p_name in provinces:
        p = 'province_' + p_name
        if r_l['province'] == p_name:
            r_df[p] = 1
        else:
            r_df[p] = 0

    return r_df


@app.route("/course_predict", methods=["POST"])
def course_predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":

        description, designation, price, region_1, variety, winery, country, province = '', '', '', '', '', '', '', ''
        request_json = flask.request.get_json()
        # if request_json["description"]:
        #     description = request_json['description']
        #
        # if request_json["designation"]:
        #     company_profile = request_json['designation']
        #
        # if request_json["price"]:
        #     benefits = request_json['price']
        #
        # if request_json["region_1"]:
        #     benefits = request_json['region_1']
        #
        # if request_json["winery"]:
        #     benefits = request_json['winery']
        #
        # if request_json["country"]:
        #     benefits = request_json['country']
        #
        # if request_json["province"]:
        #     benefits = request_json['province']

        # logger.info(f'{dt} Data: description={description}, designation={designation}, '
        #             f'price={price}, region_1={region_1}, variety={variety}, winery={winery}, country={country}, '
        #             f'province={province}')
        try:
            request_line = {
                'description': 'This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030.',
                'designation': 'Carodorum Selección Especial Reserva',
                'price': 155,
                'region_1': 'Colchagua Valley',
                'variety': 'Nerello Mascalese',
                'winery': 'Bodega Carmen Rodríguez',
                'country': 'Italy',
                'province': 'Burgundy'}

            preds = course_model.predict(get_request(request_line))
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)

        data["predictions"] = preds[0]
        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)
