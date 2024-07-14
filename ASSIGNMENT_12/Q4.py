def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")
    
    a, b = matrix[0]
    c, d = matrix[1]
    
    return a * d - b * c

matrix = [[1, 2], [3, 4]]
print(f"Determinant: {determinant_2x2(matrix)}")