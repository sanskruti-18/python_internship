# define the function
def print_price(products):
    for i in products:   # will iterate through the list
        if i['price'] > 10:
            # will print the names of the products
            print(i['name'])   

# List of the products
products = [
{'name': 'orange', 'price': 20},
{'name': 'apple', 'price': 8},
{'name': 'banana', 'price': 10},
{'name': 'kiwi', 'price': 30}
]

print("The products higher than 10 are:")
print_price(products)  # calling the function