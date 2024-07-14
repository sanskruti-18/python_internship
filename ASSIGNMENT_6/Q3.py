# print the frequency of the words that appear in the sentence
def frequency(sentence):
    sentence = sentence.lower()

    words = sentence.split()

    freq = {}  # create an empty dictionary

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

sentence = input("Enter a sentence: ")
freq = frequency(sentence)
print(freq)