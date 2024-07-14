def calculate(*args):
    minimum = min(args)
    maximum = max(args)
    average = sum(args)/len(args)

    return minimum,maximum,average

result = calculate(1,2,3,4,5,6,7,8,9,10)
print(result)