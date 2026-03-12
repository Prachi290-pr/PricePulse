import pandas as pd
import numpy as np
import sqlite3


def load_competitor_prices():

    conn = sqlite3.connect("data/pricing.db")

    df = pd.read_sql_query("SELECT competitor_price FROM competitor_prices", conn)

    conn.close()

    return df


def generate_dataset(samples=5000):

    prices_df = load_competitor_prices()

    base_prices = prices_df["competitor_price"].values

    data = []

    for _ in range(samples):

        competitor_price = np.random.choice(base_prices)

        demand = np.random.uniform(0.3, 1.0)

        inventory = np.random.randint(10, 500)

        rating = np.random.uniform(3.0, 5.0)

        season = np.random.uniform(0.5, 1.5)

        optimal_price = competitor_price * (0.9 + demand * 0.2)

        data.append([
            competitor_price,
            demand,
            inventory,
            rating,
            season,
            optimal_price
        ])

    columns = [
        "competitor_price",
        "demand",
        "inventory",
        "rating",
        "season",
        "optimal_price"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv("data/training_data.csv", index=False)

    print("Dataset created with", len(df), "samples")


if __name__ == "__main__":

    generate_dataset()