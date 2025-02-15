def calculate_cashback(spending, rewards):
    """
    Calculate cashback rewards for different credit cards.
    
    Parameters:
    spending (float): The amount spent.
    rewards (dict): A dictionary with card names as keys and reward percentages as values.
    
    Returns:
    dict: A dictionary with card names as keys and cashback earned as values.
    """
    cashback = {card: (spending * percent / 100) for card, percent in rewards.items()}
    return cashback

# Example usage:
if __name__ == "__main__":
    # Define the reward percentages for each card
    credit_cards = {
        "Card A": 1.5,  # 1.5% cashback
        "Card B": 2.0,  # 2% cashback
        "Card C": 3.0   # 3% cashback
    }
    
    # Input spending amount
    try:
        spending_amount = float(input("Enter the amount spent: "))
        if spending_amount < 0:
            raise ValueError("Spending amount cannot be negative.")
        
        # Calculate cashback
        results = calculate_cashback(spending_amount, credit_cards)
        
        # Display results
        print("\nCashback Earned:")
        for card, cashback in results.items():
            print(f"{card}: ${cashback:.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")

input("\nPress Enter to exit...")

