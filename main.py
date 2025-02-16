# elementary operations!
# op1: multiply any equation by non-zero number on both sides
def rowMult(matrix, num, row): 
    # take row to be multiplied
    multBy = matrix[i][row]

    # multiply row by num
    for i in len(matrix[i]):
        matrix = num * matrix[i][row]

    # return
    return matrix

# op2: multiply an equation by a scalar and add to another equation
def rowAdd(matrix, num, row1, row2):
    # num*row1 + row2 -> row2
    # use rowMult

    for i in matrix[i]:
        matrix = rowMult(matrix[i], num, row1) + row2[i]
    
    return matrix

def rowEchelon(matrix):
    # make 1st pivot 1
    if matrix[0] != 1:

        

    # make everything under = zero

    # do that over and over

def augmentedRowEchelon():


def inverse():


def transpose(matrix):
    result = matrix

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[j][i] = matrix[i][j]

    return result

def addMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result

def subtractMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])
    return result

def matrixMult():

def dotProd():
    

def getDeterminant():

