def longest_common_prefix(str1, str2):
    min_length = min(len(str1), len(str2))
    i = 0
    
    while i < min_length and str1[i] == str2[i]:
        i += 1
    
    return str1[:i]

input1 = input("Enter str1: ")
input2 = input("Enter str2: ")
x = longest_common_prefix(input1, input2)
print(x)