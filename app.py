
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained ML objects
model = joblib.load("models/student_model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Collect form data
        student_data = {
            "school": request.form["school"],
            "sex": request.form["sex"],
            "age": int(request.form["age"]),
            "address": request.form["address"],
            "famsize": request.form["famsize"],
            "Pstatus": request.form["Pstatus"],
            "Medu": int(request.form["Medu"]),
            "Fedu": int(request.form["Fedu"]),
            "Mjob": request.form["Mjob"],
            "Fjob": request.form["Fjob"],
            "reason": request.form["reason"],
            "guardian": request.form["guardian"],
            "traveltime": int(request.form["traveltime"]),
            "studytime": int(request.form["studytime"]),
            "failures": int(request.form["failures"]),
            "schoolsup": request.form["schoolsup"],
            "famsup": request.form["famsup"],
            "paid": request.form["paid"],
            "activities": request.form["activities"],
            "nursery": request.form["nursery"],
            "higher": request.form["higher"],
            "internet": request.form["internet"],
            "romantic": request.form["romantic"],
            "famrel": int(request.form["famrel"]),
            "freetime": int(request.form["freetime"]),
            "goout": int(request.form["goout"]),
            "Dalc": int(request.form["Dalc"]),
            "Walc": int(request.form["Walc"]),
            "health": int(request.form["health"]),
            "absences": int(request.form["absences"]),
            "G1": int(request.form["G1"]),
            "G2": int(request.form["G2"])
        }

        # Convert dictionary to DataFrame
        input_df = pd.DataFrame([student_data])

        # Apply one-hot encoding
        input_df = pd.get_dummies(
            input_df,
            drop_first=True,
            dtype=int
        )

        # Match training columns
        input_df = input_df.reindex(
            columns=features,
            fill_value=0
        )

        # Apply saved scaler
        input_scaled = scaler.transform(input_df)

        # Predict
        prediction = model.predict(input_scaled)[0]

        prediction = max(0, min(20, prediction))

        return render_template(
            "index.html",
            prediction=round(float(prediction), 2)
        )

    except (KeyError, ValueError, TypeError) as e:
        return render_template(
            "index.html",
            error="Invalid input. Please check the entered values."
        )


if __name__ == "__main__":
    app.run(debug=True)
