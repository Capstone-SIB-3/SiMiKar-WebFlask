from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import recommendation

app = Flask(__name__)
CORS(app) 
        
@app.route('/')
def home():
    return render_template ('/home.html')

if __name__=='__main__':
    app.run(debug = True)




# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# import recommendation
# import pickle
# import json
# import urllib.request
# import pandas as pd

# load the nlp model and tfidf vectorizer from disk
# filename = "./models/modelsJobs_pickle.pkl"
# clf = pickle.load(open(filename, 'rb'))
# vectorizer = pickle.load(open('./models/transform_pickle.pkl','rb'))

   
# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
# def convert_to_list(my_list):
#     my_list = my_list.split('","')
#     my_list[0] = my_list[0].replace('["','')
#     my_list[-1] = my_list[-1].replace('"]','')
#     return my_list


# convert list of numbers to list (eg. "[1,2,3]" to [1,2,3])
# def convert_to_list_num(my_list):
#     my_list = my_list.split(',')
#     my_list[0] = my_list[0].replace("[","")
#     my_list[-1] = my_list[-1].replace("]","")
#     return my_list


# def get_suggestions():
#     data = pd.read_csv('main_data.csv')
#     return list(data['movie_title'].str.capitalize())



# app = Flask(__name__)
# CORS(app) 
        
# @app.route('/')
# @app.route('/home', methods=["POST"])
# def home():
#     # getting data from AJAX request
#     jenis_pekerjaan = request.form['jenis_pekerjaan']

#     # get movie suggestions for auto complete
#     suggestions = get_suggestions()

#     #dataset
#     jobs = pd.read_csv('./techloker.csv')

#     suggestions = get_suggestions()
#     return render_template ('home.html',suggestions=suggestions,jenis_pekerjaan=jenis_pekerjaan)


# if __name__=='__main__':
#     app.run(debug = True)

# @app.route("/recommend",methods=["POST"])
# def recommend():
#     # getting data from AJAX request
#     jenis = request.form['jenis_pekerjaan']

#     # get movie suggestions for auto complete
#     suggestions = get_suggestions()

# #dataset
# jobs = pd.read_csv('./techloker.csv')

# #passing all
# return render_template()

