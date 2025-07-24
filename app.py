
from flask import Flask, request, render_template
import pickle

# Load model
with open("model/fake_news_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]
    data = [news]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)[0]
    result = "Real News" if prediction == 1 else "Fake News"
    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
