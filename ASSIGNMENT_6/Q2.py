# defining the list
x = [1,2,3]
y = [1,2,3]

# using list comprehension generating list of tuples
res = [(a,b) for a in x for b in y if a != b]

# printing the result
print(res)