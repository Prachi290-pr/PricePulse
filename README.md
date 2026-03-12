# AI Pricing Intelligence Engine

## Overview

The **AI Pricing Intelligence Engine** is an end-to-end machine learning system that analyzes competitor prices and recommends optimal product pricing using artificial intelligence.

The system simulates how companies dynamically adjust prices based on market conditions such as demand, inventory levels, seasonal trends, and competitor pricing.

This project demonstrates a **complete AI pipeline**, including data collection, storage, feature engineering, machine learning training, prediction, and analytical visualization.

---

## Key Features

* **Competitor Price Scraping**

  * Collects real product prices from an online store
  * Uses BeautifulSoup for web scraping

* **Database Pipeline**

  * Stores competitor prices and predictions in SQLite

* **Synthetic Market Data Generator**

  * Generates thousands of realistic training samples
  * Simulates market demand, product ratings, inventory levels, and seasonal trends

* **Machine Learning Model Training**

  * Trains multiple models including:

    * Linear Regression
    * Random Forest Regressor
  * Selects the best-performing model based on prediction error

* **AI Price Recommendation Engine**

  * Predicts optimal product prices using the trained model

* **AI Explanation Layer**

  * Provides natural language reasoning for pricing decisions

* **Data Visualization Dashboard**

  * Generates analytical charts for market insights

---


## Project Structure

```
ai-pricing-intelligence-engine
│
├── app
│
│   ├── scraper
│   │   └── scraper.py
│
│   ├── database
│   │   └── db.py
│
│   ├── ml
│   │   ├── dataset_generator.py
│   │   ├── train.py
│   │   └── predict.py
│
│   ├── analysis
│   │   └── feature_engineering.py
│
│   └── ai
│       └── pricing_explainer.py
│
├── data
│   └── training_data.csv
│
├── models
│   └── pricing_model.pkl
│
├── visuals
│   ├── price_distribution.png
│   ├── demand_vs_price.png
│   └── inventory_vs_price.png
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SQLite
* BeautifulSoup
* Matplotlib
* Seaborn

---

## Example Output

```
Competitor Average Price: 38.05
AI Recommended Price: 40.96

AI Explanation:
Competitor average price is 38.05.
Market demand is high.
Product rating is strong.
AI recommends pricing slightly above competitors due to strong demand.
```

---

## Generated Visualizations

The project generates analytical charts including:

* Competitor price distribution
* Demand vs optimal price
* Inventory vs optimal price

These visualizations help analyze pricing behavior and market trends.

---

## How to Run the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the scraper

```
python -m app.scraper.scraper
```

### 3. Generate the dataset

```
python -m app.ml.dataset_generator
```

### 4. Train the machine learning model

```
python -m app.ml.train
```

### 5. Run the AI pricing engine

```
python -m app.ml.predict
```

---


