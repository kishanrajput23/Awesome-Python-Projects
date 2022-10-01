import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('pac.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl','rb'))

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	news = request.form['news']
    	data = [news]
    	vect = tfidf.transform(data)
    	my_prediction = model.predict(vect)
    	return render_template('prediction.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)
