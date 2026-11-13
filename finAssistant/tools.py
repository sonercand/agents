def calculate_percentage_change(initial_value: float, final_value: float) -> float:
    """Calculates the percentage change between two numbers."""
    if initial_value == 0:
        return 0.0
    return ((final_value - initial_value) / initial_value) * 100.0


def calculate_profit_or_loss(number_of_shares: int, purchase_price: float, current_price: float) -> float:
    """Calculates the profit or loss from a stock transaction."""
    return number_of_shares * (current_price - purchase_price)