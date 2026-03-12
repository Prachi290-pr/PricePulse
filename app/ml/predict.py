import sqlite3
import pandas as pd
import numpy as np
import joblib

from app.database.db import insert_prediction
from app.ai.pricing_explainer import explain_price

def load_competitor_prices():

    conn = sqlite3.connect("data/pricing.db")

    df = pd.read_sql_query(
        "SELECT competitor_price FROM competitor_prices",
        conn
    )

    conn.close()

    return df


def predict_price():

    df = load_competitor_prices()

    avg_price = df["competitor_price"].mean()

    demand = np.random.uniform(0.5, 1.0)

    inventory = np.random.randint(50, 300)

    rating = np.random.uniform(3.5, 5.0)

    season = np.random.uniform(0.8, 1.2)

    features = pd.DataFrame([[
        avg_price,
        demand,
        inventory,
        rating,
        season
    ]], columns=[
        "competitor_price",
        "demand",
        "inventory",
        "rating",
        "season"
    ])

    model = joblib.load("models/pricing_model.pkl")

    predicted_price = model.predict(features)[0]

    print("Competitor Average Price:", round(avg_price, 2))
    print("AI Recommended Price:", round(predicted_price, 2))

    insert_prediction("Book Product", predicted_price)

    
    explanation = explain_price(avg_price, predicted_price, demand, rating)

    print("\nAI Explanation:")
    print(explanation)


if __name__ == "__main__":

    predict_price()
