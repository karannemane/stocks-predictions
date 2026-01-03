from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)  # allow frontend access

@app.route("/")
def home():
    return "Indian Stock Prediction API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symbol = data.get("symbol")

    if not symbol:
        return jsonify({"error": "Stock symbol required"}), 400

    try:
        # NSE stocks require .NS
        stock = yf.download(symbol + ".NS", period="1y")

        stock = stock[['Open', 'High', 'Low', 'Volume', 'Close']]
        stock.dropna(inplace=True)

        X = stock[['Open', 'High', 'Low', 'Volume']]
        y = stock['Close']

        model = LinearRegression()
        model.fit(X, y)

        last_row = X.iloc[-1].values.reshape(1, -1)
        prediction = model.predict(last_row)[0]

        return jsonify({
            "stock": symbol,
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
