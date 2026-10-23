from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import pickle
import os

model_path= os.path.join (settings.BASE_DIR, "Model.pkl")
with open (model_path,"rb") as file:
    model = pickle.load(file)

def home(request) :
    return HttpResponse("Home Page - ML39")

def about(request) :
    return HttpResponse("About Page - ML39")

def contact(request) :
    return HttpResponse("Contact Page - ML39")


def base(request) :
    prediction = None

    if request.method == "POST":
        age = request.POST.get ('age')
        gender = request.POST.get('gender')
        hormones= request.POST.get ('hormones')
        history = request.POST.get ('history')
        weight= request.POST.get('weight')
        calcium = request.POST.get('calcium')
        activity = request.POST.get('activity')
        smoking = request.POST.get('smoking')
        medcondition = request.POST.get ('medcondition')
        fractures = request.POST.get ('fractures')

        if age: age = int(age)
        gender = int(gender)
        hormones = int (hormones)
        history = int (history)
        weight = int(weight)
        calcium = int(calcium)
        activity = int(activity)
        smoking = int(smoking)
        medcondition = int(medcondition)
        fractures = int(fractures)

        features=[[age, gender, hormones, history, weight, calcium, activity, smoking, medcondition, fractures]]
        prediction =model.predict(features)[0]

        prediction_map = {
            0: "Less Chances of Osteoporosis",
            1: "More Chances of Osteoporosis"
        }

        prediction = prediction_map.get(prediction, "unknown")

    return render (request, 'index.html',{"prediction": prediction})

