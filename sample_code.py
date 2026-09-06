def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price


products = [
    {"name": "Laptop", "price": 1200, "discount": 10},
    {"name": "Headphones", "price": 150, "discount": 20},
    {"name": "Keyboard", "price": -80, "discount": 150},
]

for product in products:
    price = calculate_discount(
        product["price"],
        product["discount"]
    )

    print(product["name"], "Final price:", price)