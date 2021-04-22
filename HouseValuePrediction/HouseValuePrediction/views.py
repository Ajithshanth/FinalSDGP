from django.shortcuts import render
import numpy as np
import joblib

getModel = joblib.load('./models/finalized_model.sav')

def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    var_a  = float(request.GET['n1'])   #Bedrooms
    var_b  = float(request.GET['n2'])   #Bathrooms
    var_c  = float(request.GET['n3'])   #Square Feet of House
    var_d  = float(request.GET['n4'])   #Square Feet of Land
    var_e  = float(request.GET['n5'])   #Floors
    var_f  = float(request.GET['n6'])   #Swimming Pool
    var_g  = float(request.GET['n7'])   #People Viewed the House
    var_h  = float(request.GET['n8'])   #Rating
    var_i  = float(request.GET['n9'])   #Grade
    var_j = float(request.GET['n10'])   #Square Feet of House apart From Basement
    var_k = float(request.GET['n11'])   #Square Feet of Basement
    var_l = float(request.GET['n12'])   #Built Year
    var_m = float(request.GET['n13'])   #Renovated Year
    var_n = float(request.GET['n14'])   #Zipcode
    var_o = float(request.GET['n15'])   #Latitude
    var_p = float(request.GET['n16'])   #Longitude
    var_q = float(request.GET['n17'])   #Square Feet of House after renovation
    var_r = float(request.GET['n18'])   #Square Feet of Land after renovation

    #renovated year must be after the built year
    #Sqft of house is equal to sqft of house apart from the basement + sqft of basement

    if (var_l < var_m) or (var_m ==0) :

        predict1 = getModel.predict(np.array([var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h, var_i, var_j, var_k, var_l, var_m, var_n, var_o, var_p, var_q, var_r]).reshape(1, -1))
        predict1 = round(predict1[0])
        price = "${:,.2f}".format(predict1)
        value1 = "The predicted value is " + price


        return render(request, "predict.html", {"result2": value1 } )

    else:
        return render(request, "predict.html", {"result2": "Please Enter Appropriate Values"})


