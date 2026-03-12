import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def train_model():

    df = pd.read_csv("data/training_data.csv")

    X = df.drop("optimal_price", axis=1)
    y = df["optimal_price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    lr_preds = lr.predict(X_test)
    lr_error = mean_squared_error(y_test, lr_preds)

    # Random Forest
    rf = RandomForestRegressor(n_estimators=100)
    rf.fit(X_train, y_train)

    rf_preds = rf.predict(X_test)
    rf_error = mean_squared_error(y_test, rf_preds)

    print("Linear Regression MSE:", lr_error)
    print("Random Forest MSE:", rf_error)

    if rf_error < lr_error:
        best_model = rf
        print("Random Forest selected")
    else:
        best_model = lr
        print("Linear Regression selected")

    joblib.dump(best_model, "models/pricing_model.pkl")

    print("Model saved to models/pricing_model.pkl")


if __name__ == "__main__":

    train_model()