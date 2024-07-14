product_quantities = [13, 5, 6, 10, 11]
prices = [1.2, 6.5, 1.0, 4.8, 5.0]

# Method 1
# using list comprehension
total = [product_quantities[i]*prices[i] for i in range(len(prices))]

total_sum = 0
for price in total:
    total_sum += price

print(total_sum)

# Method 2
# using list comprehension 
total_price = sum([i*j for i,j in zip(product_quantities, prices)])
# used zip function to pair the list for corresponding values
# used sum function to add the product

print(total_price)