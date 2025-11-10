product = input("Enter the product name: ")
price = float(input("Enter the product price: "))

if price > 10000:
    discount = 0.20
elif price >= 5000 and price <= 10000:
    discount = 0.10 
else:
    discount = 0.00
discounted_price = price - (price * discount)
print(f"The {product} now costs {discounted_price:.2f} KES after discount.")
