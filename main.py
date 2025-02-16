import numpy as np
''''
for Matrix.columns in Matrix.data:
    for Matrix.rows in Matrix.data:
'''

exampleData =   np.array([[1, 1, 4, 0],
                        [1, 2, -3, -2],
                        [3, 8, -23, -9]])


# elementary operations
# op1: multiply any equation by non-zero number on both sides
def op1(data, num, row):
    data = np.array(data)
    for i in range(0, len(data[0])):
        data[i:i][row:row] = num * data[i:i][row:row]

print(exampleData)
op1(exampleData, 10, 1)
print(exampleData)

# op2: multiply an equation by a scalar and add to another equation
# def op2(data):

def rowEchelon():

def augmentedRowEchelon():

def inverse():

def transpose():

def addMatrix():

def subtractMatrix():

def matrixMult():

def dotProd():

def getDeterminant():

