from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import ensemble



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

        data = pd.read_csv(r"/HouseValuePrediction/HouseValuePrediction/Data/kc_house_data.csv")
        data = data.drop(["id", "date"], axis=1)

        X = data.drop("price", axis=1)
        Y = data["price"]

        X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.10,random_state =2)

        lr_model = LinearRegression()
        lr_model.fit(X_train, Y_train)

        gbr_model = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                                 learning_rate=0.1, loss='ls')
        gbr_model.fit(X_train, Y_train)

        pred1 = gbr_model.predict(np.array([var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h, var_i, var_j, var_k, var_l, var_m, var_n, var_o, var_p, var_q, var_r]).reshape(1, -1))
        pred1 = round(pred1[0])
        price = "${:,.2f}".format(pred1)
        value1 = "The predicted value is " + price

        #pred2 = gbr.predict(np.array([var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h, var_i, var_j, var_k, var_l, var_m, var_n, var_o, var_p, var_q, var_r]).reshape(1, -1))
        #pred2 = round(pred2[0])
        #value2 = "The predicted value is $" + str(pred2)

        return render(request, "predict.html", {"result2": value1 } )

    else:
        return render(request, "predict.html", {"result2": "Please Enter Appropriate Values"})


