import random
import string

def random_alpha_char():
    return random.choice(string.ascii_letters)

def random_alpha_string(length=None):
    if length is None:
        length = random.randint(1,100)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def fixed_length_alpha_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

print(random_alpha_char())
print(random_alpha_string())
print(fixed_length_alpha_string(10))