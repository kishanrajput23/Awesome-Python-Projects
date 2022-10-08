from django.shortcuts import render, render
import base64



import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import numpy as np

model = tensorflow.keras.models.load_model('/home/Linux/Predict_types_of_arrhythmia.h5')
# model = tensorflow.keras.models.load_model('C:\\Users\\divya\\Desktop\\ECG_TO_IMAGE\\Trained Models\\Predict_types_of_arrhythmia.h5')
print('loaded model')


# Create your views here.

def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        inImg = request.FILES['myfile'].read()

        encoded = base64.b64encode(inImg).decode('ascii')
        mime = "image/jpg"
        mime = mime + ";" if mime else ";"
        input_image = "data:%sbase64,%s" % (mime, encoded)

        image = load_img(request.FILES['myfile'], target_size=(224, 224))

        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image /= 255.

        pred = model.predict(image.reshape((1, 224, 224, 3)))
        pred_class = pred.argmax(axis=1)

        # folder order 'L' 'N' 'P' 'R' 'V'

        type = ""
        status = 0
        probability = str(pred[0][pred_class]).strip('[]')

        if pred_class == 1:
            type = 'Left bundle branch block beat'
        elif pred_class == 2:
            type = 'Normal heartbeat'
            status = 1
        elif pred_class == 3:
            type = 'Paced beat'
        elif pred_class == 4:
            type = 'Right bundle branch block beat'
        elif pred_class == 5:
            type = 'Premature ventricular contraction'

        print("probability = ", probability)

        context = {
            'image': input_image,
            'status': status,
            'accuracy': float(probability)*100,
            'type': type
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html')




def temp(request):
    return render(request, 'test.html')
