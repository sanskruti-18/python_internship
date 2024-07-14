import random

def create_random_int_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def select_random_items(lst, k):
    return random.sample(lst, k)

def main():
    # Parameters
    list_size = 20
    lower_bound = 1
    upper_bound = 100
    k = 5
    
    # Created a list of random integers
    random_list = create_random_int_list(list_size, lower_bound, upper_bound)
    print(f"Random List: {random_list}")
    
    # Selected k random items from the list
    selected_items = select_random_items(random_list, k)
    print(f"Selected Items: {selected_items}")

if __name__ == "__main__":
    main()
