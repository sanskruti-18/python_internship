
# random module is used to generate random numbers
import random
# collection module is used to count the occurrences of elements
from collections import Counter

# define function
def roll_die(times):
    rolls = [random.randint(1,6) for _ in range(times)]  # runs for 500 times
    return rolls   # returns the list of rolls

# define funciton
def count(rolls):
    roll_counts = Counter(rolls)
    return roll_counts   # returns the count

# define th emain function
def main():
    times = 500
    rolls = roll_die(times)
    roll_counts = count(rolls)

    for face in range(1,7):
        print(f"{face} : {roll_counts[face]} times")

# checks if the program is run directly and not from module
if __name__ == "__main__":
    main()