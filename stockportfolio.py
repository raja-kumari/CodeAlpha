 #Stock Portfolio Tracker


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300
}

print("📊 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
          
portfolio = {}

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found in our list. Please try again.")


total = 0
print("\n🧾 Your Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total += investment
    print(f"{stock}: {quantity} shares x ${price} = ${investment}")

print(f"\n💰 Total investment value: ${total}")


save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save_option == 'yes':
    with open("portfolio.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity} shares at ${stock_prices[stock]} each\n")
        file.write(f"\nTotal investment value: ${total}")
    print("✅ Portfolio saved to portfolio.txt")
else:
    print("Portfolio not saved.")

print("\n✅ Thank you for using the Stock Portfolio Tracker!")
