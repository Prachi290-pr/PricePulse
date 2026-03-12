def explain_price(avg_price, predicted_price, demand, rating):

    explanation = []

    explanation.append(f"Competitor average price is {round(avg_price,2)}.")

    if demand > 0.7:
        explanation.append("Market demand is high.")
    else:
        explanation.append("Market demand is moderate.")

    if rating > 4:
        explanation.append("Product rating is strong.")

    if predicted_price > avg_price:
        explanation.append(
            "AI recommends pricing slightly above competitors due to strong demand."
        )
    else:
        explanation.append(
            "AI recommends pricing slightly below competitors to stay competitive."
        )

    return " ".join(explanation)