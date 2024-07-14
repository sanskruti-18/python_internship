# define the function
def count_letters_and_digits(str):
    alphabet_count = 0
    digit_count = 0
    for i in str:
        if i.isalpha():
            alphabet_count = alphabet_count + 1
        if i.isdigit():
            digit_count = digit_count + 1
        else:
            pass

    # print the output
    print(f"Letters: {alphabet_count}")
    print(f"Digits: {digit_count}")

# input the string
str = input("Enter a sentence:")
count_letters_and_digits(str)  # calling the function