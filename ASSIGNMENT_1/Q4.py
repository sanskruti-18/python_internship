def find_opposite_face(face_number):
    if 1 <= face_number <= 6:
        return 7 - face_number
    else:
        return None  # for invalid face number

# Taking the dice face number as input from user
face_number = int(input("Enter a dice face number (1-6): "))

# Finding the opposite face number
opposite_face = find_opposite_face(face_number)

# print the result
if opposite_face != None:
    print(f"The opposite face of {face_number} is {opposite_face}")
else:
    print("Invalid face number. Please enter a number between 1 and 6.")
