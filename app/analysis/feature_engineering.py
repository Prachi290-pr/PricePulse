import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_visualizations():

    df = pd.read_csv("data/training_data.csv")

    # Price distribution
    plt.figure()
    sns.histplot(df["competitor_price"], bins=30)
    plt.title("Competitor Price Distribution")
    plt.savefig("visuals/price_distribution.png")

    # Demand vs optimal price
    plt.figure()
    sns.scatterplot(x=df["demand"], y=df["optimal_price"])
    plt.title("Demand vs Optimal Price")
    plt.savefig("visuals/demand_vs_price.png")

    # Inventory vs optimal price
    plt.figure()
    sns.scatterplot(x=df["inventory"], y=df["optimal_price"])
    plt.title("Inventory vs Optimal Price")
    plt.savefig("visuals/inventory_vs_price.png")

    print("Visualizations saved in visuals folder")


if __name__ == "__main__":

    generate_visualizations()