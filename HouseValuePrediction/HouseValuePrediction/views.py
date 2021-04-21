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
    var_a  = float(request.GET['n1'])
    var_b  = float(request.GET['n2'])
    var_c  = float(request.GET['n3'])
    var_d  = float(request.GET['n4'])
    var_e  = float(request.GET['n5'])

    var_f  = float(request.GET['n6'])
    var_g  = float(request.GET['n7'])
    var_h  = float(request.GET['n8'])
    var_i  = float(request.GET['n9'])
    var_j = float(request.GET['n10'])
    var_k = float(request.GET['n11'])
    var_l = float(request.GET['n12'])
    var_m = float(request.GET['n13'])
    var_n = float(request.GET['n14'])
    var_o = float(request.GET['n15'])
    var_p = float(request.GET['n16'])
    var_q = float(request.GET['n17'])
    var_r = float(request.GET['n18'])


    if(1==1):
        data = pd.read_csv(r"C:/Users/Ajith/Desktop/Final SDGP/HouseValuePrediction/kc_house_data.csv")
        data = data.drop(["id", "date"], axis=1)
        x = data.drop("price", axis=1)
        y = data["price"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.30)
        model = LinearRegression()
        model.fit(x_train, y_train)
        pred = model.predict(np.array([var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h, var_i, var_j, var_k, var_l, var_m, var_n, var_o, var_p, var_q, var_r]).reshape(1, -1))
        pred = round(pred[0])
        value = "The predicted value is $" + str(pred)
        return render(request, "predict.html", {"result2": value})
    else:
        return render(request, "predict.html", {"result2": "Please Enter Appropriate Values"})

