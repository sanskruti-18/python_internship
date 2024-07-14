def find_consonants(string):
    consonants = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]  # Define vowels

    for char in string:
        # Check if character is an alphabet and not a vowel
        if char.isalpha() and char not in vowels:
            consonants.append(char)

    return consonants

# take the input from the user 
string = input("Enter a string:")
consonant_list = find_consonants(string)

print("Consonants in the string:", consonant_list)