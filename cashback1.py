def calculate_best_card(spending, category):
    """
    Determine the best credit card for a given spending category and calculate cashback.
    
    Parameters:
    spending (float): The amount spent.
    category (str): The category of spending.
    
    Returns:
    tuple: Best card name, cashback earned, and cashback rate.
    """
    food_keywords = ["food", "restaurant", "burger", "pizza", "sandwich", "taco", "turkey", "steak", "sushi", "fries", "noodles", "chicken", "salad", "hot dog", "bbq", "wings", "curry", "burrito", "sub", "donut", "bagel", "cake", "pie", "dessert"]
    grocery_keywords = ["grocery", "groceries", "supermarket", "milk", "bread", "vegetables", "fruits", "eggs", "cheese", "butter", "yogurt", "pasta"]
    gas_keywords = ["gas", "fuel", "petrol"]
    
    # Normalize the input category to lower case for comparison
    category = category.lower()

    # Assign category based on keywords
    if any(keyword in category for keyword in food_keywords):
        category = "food"
    elif any(keyword in category for keyword in grocery_keywords):
        category = "grocery"
    elif any(keyword in category for keyword in gas_keywords):
        category = "gas"
    else:
        category = "other"
    
    rewards = {
        "Citi Card": {"food": 5.0},
        "Venmo Card": {"grocery": 3.0},
        "Sams Club Card": {"gas": 5.0},
        "Wells Fargo Card": {"other": 2.0}
    }
    
    best_card = "Wells Fargo Card"  # Default to 2% for "other" purchases
    best_rate = 2.0
    
    # Find the best card and rate
    for card, categories in rewards.items():
        if category in categories:
            best_card = card
            best_rate = categories[category]
            break
    
    cashback = spending * best_rate / 100
    return best_card, cashback, best_rate, category

# Example usage:
if __name__ == "__main__":
    try:
        spending_amount = float(input("How much are you spending?: "))
        if spending_amount < 0:
            raise ValueError("Spending amount cannot be negative.")
        
        category = input("What are you buying?: ").strip().lower()
        
        best_card, cashback, best_rate, category = calculate_best_card(spending_amount, category)
        
        print("\n" + "-" * 16)
        
        if category == "food":
            print(f"Use the Citi Card because you'll get back {best_rate}% on food.")
        elif category == "grocery":
            print(f"Use the Venmo Card because you'll earn {best_rate}% back on groceries.")
        elif category == "gas":
            print(f"Use the Sams Club Card because you'll get back {best_rate}% on gas.")
        else:
            print(f"Use the Wells Fargo Card, earning {best_rate}% on all other purchases.")
        
        print(f"You will earn ${cashback:.2f} in cashback.")
        print("-" * 16 + "\n")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
