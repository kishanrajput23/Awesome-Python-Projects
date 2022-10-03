from django.shortcuts import render
import joblib
from sklearn.svm import SVC

# Create your views here.

def home(request):
    return render(request, 'home.html')

def submit(request):
    if request.method == 'POST':
        g = request.POST['gender']
        if g == "male":
            gender = 0
        else:
            gender = 1
        height = request.POST['height']
        weight = request.POST['weight']

        temp = []
        temp.append(gender)
        temp.append(height)
        temp.append(weight)
        print(temp)

        pred = []
        pred.append(temp)
        print(pred)


        filename = 'linear_SVM_classifier.sav'
        model = joblib.load(filename)

        prediction = model.predict(pred)
        output = ""

        if str(prediction) == "[0]":
            output = "Extremely weak"
            status = 0
        elif str(prediction) == "[1]":
            output = "Weak"
            status = 1
        elif str(prediction) == "[2]":
            output = "Normal"
            status = 2
        elif str(prediction) == "[3]":
            output = "Overweight"
            status = 3
        elif str(prediction) == "[4]":
            output = "Obese"
            status = 4
        elif str(prediction) == "[5]":
            output = "Extremely Obese"
            status = 5


        print("output = ", output)

        context = {
            'gender': g,
            'height': height,
            'weight': weight,
            'response': output,
            'status': status
        }

    return render(request, 'home.html', context)

