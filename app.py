from flask import Flask, request, render_template
import numpy
from datetime import datetime
from classifier import load_model

app = Flask(__name__)

# Load model once at startup
model = load_model()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form

        # ---------- Numeric inputs ----------
        showroom_price = float(data.get("showroom_price", 0))
        kms_driven = float(data.get("kms_driven", 0))
        owners = float(data.get("owners", 0))
        year = int(data.get("year", 0))

        # ---------- Categorical encoding ----------
        fuel_map = {
            "Petrol": 0,
            "Diesel": 1,
            "CNG": 2
        }

        seller_map = {
            "Dealer": 0,
            "Individual": 1
        }

        transmission_map = {
            "Manual": 0,
            "Automatic": 1
        }

        fuel = fuel_map.get(data.get("fuel"), 0)
        seller = seller_map.get(data.get("seller_type"), 0)
        transmission = transmission_map.get(data.get("transmission"), 0)

        # ---------- Derived feature ----------
        current_year = datetime.now().year
        age = current_year - year

        # ---------- Feature vector ----------
        features = [
            showroom_price,
            kms_driven,
            owners,
            age,
            fuel,
            seller,
            transmission,
            1.0   # constant feature (matches your training data)
        ]

        final_features = numpy.array([features])

        # ---------- Prediction ----------
        prediction = model.predict(final_features)[0]

        output = f"Predicted Selling Price: ₹ {prediction:.2f} Lakhs"

        return render_template(
            "index.html",
            prediction_text=output
        )

    except Exception as e:
        # If anything goes wrong — show message instead of crash
        return render_template(
            "index.html",
            prediction_text="⚠️ Error in prediction. Please check your inputs."
        )


if __name__ == "__main__":
    app.run(debug=True)
