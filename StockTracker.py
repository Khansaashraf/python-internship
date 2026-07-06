"""
****Simple Stock Tracker****

- User inputs stock names and quantities.
- Stock prices are hardcoded in a dictionary.
- Calculates total investment value.
- Saves the result to a .csv file.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (per share)
STOCK_PRICES = {
    "APPL": 180,
    "TSLA": 250,
    "GOGL": 140,
    "AMZN": 130,
    "MSFT": 330,
}


def get_user_holdings():
    """Ask the user for stock names and quantities until they're done."""
    holdings = {}

    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")

    print("\nEnter stock holdings (type 'done' as the stock name to finish).")

    while True:
        name = input("\nStock name: ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print(f"'{name}' not found in price list. Try one of: {', '.join(STOCK_PRICES)}")
            continue

        qty_input = input(f"Quantity of {name}: ").strip()

        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity.")
            continue

        qty = int(qty_input)

        # Add to existing quantity if the stock was already entered (handles duplicate)
        holdings[name] = holdings.get(name, 0) + qty

    return holdings


def calculate_investment(holdings):
    """Calculate per-stock value and total investment."""
    details = []
    total = 0

    for stock, qty in holdings.items(): #Loops through every stock the user entered.
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value          #For each one: looks up the price from STOCK_PRICES, multiplies by quantity, accumulates the running total.
        details.append({"stock": stock, "quantity": qty, "price": price, "value": value})

    return details, total #Returns a list of dictionaries (one per stock) and the grand total.


def display_summary(details, total):
    print("\n--- Investment Summary ---")
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    for row in details:
        print(f"{row['stock']:<8}{row['quantity']:<8}${row['price']:<9}${row['value']:<9}")
    print("-" * 34)
    print(f"Total Investment: ${total}")


def save_to_csv(details, total, filename="investment_summary.csv"):
    """Save the summary to a CSV file."""
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for row in details:
            writer.writerow([row["stock"], row["quantity"], row["price"], row["value"]])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
        writer.writerow(["Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    print(f"\nSummary saved to '{filename}'")


def main(): # ties everything together in order — collect → calculate → display → (optionally) save.
    holdings = get_user_holdings()

    if not holdings:
        print("\nNo holdings entered. Exiting.")
        return

    details, total = calculate_investment(holdings)
    display_summary(details, total)

    save_choice = input("\nSave summary to a CSV file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_to_csv(details, total)


if __name__ == "__main__":
    main()