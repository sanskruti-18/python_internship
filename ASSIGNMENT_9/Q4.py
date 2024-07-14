def word_length_dict(sentence):
    # spliting the sentence into words
    words = sentence.split()
    return {word: len(word) for word in words}

# taking input form the user
sentence = input("Enter a sentence: ")
# calling the funciton
print(word_length_dict(sentence))