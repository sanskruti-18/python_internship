# define the dunction
def calculate_discounted_price(original_price, discount_percent):
    # print error is price is in negative and discount in not in between 0 to 100
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100")

    # calculation of discounted price
    discount_amount = original_price * (discount_percent / 100)
    discounted_price = original_price - discount_amount
    return discounted_price

# taking input from the user
original_price = int(input("Enter the price of the product: "))
discount_percent = int(input("Enter the discount offered: "))
print(calculate_discounted_price(original_price, discount_percent)) # calling the funciton
