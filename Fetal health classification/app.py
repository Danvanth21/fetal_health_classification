#Importing required Libraries
#flask for API development
from flask import Flask, request, render_template
#requests and bs4 for web scraping
import requests

#pickle for reading .pkl file
import pickle
#numpy for array
import numpy as np

#web scraping for dollar value in INR


#reading .pkl file
path='dpp.pkl'
model = pickle.load(open(path, 'rb'))

#creating instance for Flask 
app=Flask(__name__)
app.secret_key="diam1234"

#getting input from frontend
@app.route('/input',methods=['GET','POST'])
def input():
    details=request.form
    #getting carat, cut, color, clarity, depth and table as input to predict diamond price
    baseline_value= float(details['baseline_value'])
    accelerations= int(details['accelerations'])
    fetal_movement = int(details['fetal_movement'])
    uterine_contractions = int(details['uterine_contractions'])
    light_decelerations=float(details['light_decelerations'])
    severe_decelerations=float(details['severe_decelerations'])
    prolongued_decelerations=float(details['prolongued_decelerations'])
    abnormal_short_term_variability=float(details['abnormal_short_term_variability'])
    mean_value_of_short_term_variability=float(details['mean_value_of_short_term_variability'])
    percentage_of_time_with_abnormal_long_term_variability=float(details['percentage_of_time_with_abnormal_long_term_variability'])
    mean_value_of_long_term_variability=float(details['mean_value_of_long_term_variability'])
    histogram_width=float(details['histogram_width'])
    histogram_min=float(details['histogram_min'])
    histogram_max=float(details['histogram_max'])
    histogram_number_of_peaks=float(details['histogram_number_of_peaks'])
    histogram_number_of_zeroes=float(details['histogram_number_of_zeroes'])
    histogram_mode=float(details['histogram_mode'])
    histogram_mean=float(details['histogram_mean'])
    histogram_median=float(details['histogram_median'])
    histogram_variance=float(details['histogram_variance'])
    histogram_tendency=float(details['histogram_tendency'])
    
  
    prediction=model.predict([[baseline_value ,accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations ,prolongued_decelerations  , abnormal_short_term_variability  , mean_value_of_short_term_variability  , percentage_of_time_with_abnormal_long_term_variability ,mean_value_of_long_term_variability  , histogram_width , histogram_min  , histogram_max  , histogram_number_of_peaks  , histogram_number_of_zeroes  , histogram_mode  , histogram_mean  , histogram_median  , histogram_variance  , histogram_tendency]])
    #converting dollar to INR using web scraped data
    pred=''
    if (prediction == True):
        pred="At Risk"
    else:
        pred="Normal"

    msg="Fetal Health Predicted as "+str(pred)
    # print(msg)
    #rendering price to output page
    return render_template('output.html', msg=msg)

#rendering to input page
@app.route('/')
def submit():
    return render_template('input.html')
#main function
if __name__ == '__main__':
    app.run(debug=True)
