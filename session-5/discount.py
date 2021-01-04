"""
In this challenge, you must discount a price according to its value.

    • If the price is 300 or above, there will be a 30% discount.
    • If the price is between 200 and 300(200 inclusive), there will be a 20% discount.
    • If the price is between 100 and 200(100 inclusive), there will be a 10% discount.
    • If the price is less than 100, there will be a 5% discount.
    • If the price is negative, there will be no discount.

The price after a discount would be price * (1 - discount).
"""

# Let's say the price of a product is 250
price = 250

# make discounts to the price accordingly

# check which discount is approprite for the price
if price >= 300:
    price *= 0.7
elif price >= 250:
    price *= 0.8
elif price >= 100:
    price *= 0.9
elif price < 100:
    price *= 0.95


print(price)

"""
Keep in mind that price *= 0.7 is just a short form of the following

price = price * 0.7
"""
