def find_character(matrix, char):
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == char:
                print(f"Character found at row {row_index}, column {col_index}")
                return
    print("Not found")

def main():
    # Take matrix input from the user
    rows = int(input("Enter the number of rows: "))
    matrix = []
    print("Enter the elements row by row, separated by spaces:")
    for _ in range(rows):
        row = input().split()
        matrix.append(row)

    # Print the matrix
    print("\nMatrix:")
    for row in matrix:
        print(' '.join(row))

    # Take character input from the user
    char = input("\nEnter a character to find: ")
    
    # Find and print the character's position(matrix, char)

if __name__ == "__main__":
    main()