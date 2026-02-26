
from flask import Flask, render_template, request
import pickle
import matplotlib.pyplot as plt
import io
import base64
from ai_suggestion import get_ai_suggestion

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

history = []
stats = {"Positive": 0, "Negative": 0}

risk_keywords = [
    "suicide", "kill myself", "end my life",
    "self harm", "die", "no reason to live"
]

def detect_risk(text):
    text = text.lower()
    for word in risk_keywords:
        if word in text:
            return True
    return False

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    suggestion = None
    chart = None

    if request.method == "POST":
        text = request.form["user_input"]

        if detect_risk(text):
            prediction = "High Risk"
            suggestion = "Please talk to a trusted adult, guardian, or a mental health professional immediately. You are not alone."
        else:
            prediction = model.predict([text])[0]
            history.append(prediction)
            stats[prediction] += 1

            if prediction == "Negative":
                suggestion = get_ai_suggestion(text)

    # Create analytics chart
    fig, ax = plt.subplots()
    ax.bar(stats.keys(), stats.values())
    ax.set_title("Prediction Distribution")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)

    return render_template("index.html",
                           prediction=prediction,
                           suggestion=suggestion,
                           chart=chart,
                           history=history[-10:])

if __name__ == "__main__":
    app.run(debug=True)
