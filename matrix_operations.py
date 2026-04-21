# Input dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Function to get matrix input from user
def get_matrix(rows, cols, name):
    print(f"\nEnter entries for {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            n = int(input(f"Enter element for {name} at [{i}][{j}]: "))
            row.append(n)
        matrix.append(row)
    return matrix

# Get two matrices
matrix_a = get_matrix(rows, cols, "Matrix A")
matrix_b = get_matrix(rows, cols, "Matrix B")

# Perform Addition 
import numpy as np 
a=np.array(matrix_a)
b=np.array(matrix_b)

add=a+b
print("addition:", add)

sub=a-b
print("subtraction:", sub)

print("transpose of a matrix: ", np.transpose(matrix_a))

