def stock_portfolio():
    prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOG": 140.0,
        "INFY": 1550.0,
        "TCS": 3900.0
    }

    total_value = 0.0

    print("Simple Stock Portfolio Tracker")
    print("Available stocks and prices:")
    for name, price in prices.items():
        print(f"{name}: {price} per share")

    while True:
        name = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        if name == "DONE":
            break

        if name not in prices:
            print("Stock not found in price list.")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid integer quantity.")
            continue

        value = prices[name] * qty
        total_value += value
        print(f"Added {qty} of {name}, value = {value}")

    print(f"\nTotal portfolio value = {total_value}")

if __name__ == "__main__":
    stock_portfolio()
