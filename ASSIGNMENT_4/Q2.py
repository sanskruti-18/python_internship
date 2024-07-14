# Method 1
matrix1 = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
matrix2 = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
res = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(matrix1)):   
# iterate through columns
    for j in range(len(matrix1[0])):
        res[i][j] = matrix1[i][j] + matrix2[i][j]
 
for r in res:
    print(r)



# Method 2
def input_matrix(mat1, mat2, r1, c1, r2, c2):
    print("Enter values for matrix 1: ")
    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(int(input()))
        mat1.append(a)

    print("Enter the values for matrix 2:")
    for i in range(r2):
        b = []
        for j in range(c2):
            b.append(int(input()))
        mat2.append(b)

def print_matrix(mat1, mat2, r1, c1, r2, c2):
    print("Matrix 1:")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j], end = " ")
        print()

    print("Matrix 2:")
    for i in range(r2):
        for j in range(c2):
            print(mat2[i][j], end = " ")
        print()

def add_matrix(mat1, mat2, r1, c1, r2, c2, res):
    if r1 == r2 and c1 == c2:
        for i in range(r1):   
            for j in range(c1):
                res[i][j] = mat1[i][j] + mat2[i][j]
        print("The resultant matrix is:")
        for i in range(r1):
            for j in range(c1):
                print(res[i][j], end = " ")
            print()
    else:
        print("The matrices cannot be added")

r1 = int(input("Enter the number of rows for matrix 1: "))
c1 = int(input("Enter the number of coloumns for matrix 1: "))
r2 = int(input("Enter the number of rows for matrix 2: "))
c2 = int(input("Enter the number of coloumns for matrix 2: "))

mat1 = []
mat2 = []
res = [[0 for j in range(c1)] for i in range(r1)]
input_matrix(mat1, mat2, r1, c1, r2, c2)
print_matrix(mat1, mat2, r1, c1, r2, c2)
add_matrix(mat1, mat2, r1, c1, r2, c2, res)