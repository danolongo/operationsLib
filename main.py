# elementary operations!
# op1: multiply any equation by non-zero number on both sides
def rowMult(arr, num, row): 
    # take row to be multiplied
    multBy = arr[i][row]

    # multiply row by num
    for i in len(arr[i]):
        arr = num * arr[i][row]

    # return
    return arr

# op2: multiply an equation by a scalar and add to another equation
def rowAdd(arr1, num, row1, row2):
    # num*row1 + row2 -> row2
    # use rowMult

    for i in arr1[i]:
        arr1 = rowMult(arr1[i], num, row1) + row2[i]
    
    return arr1

def rowEchelon():
    # make 1st pivot 1
    

    # make everything under = zero

    # do that over and over

def augmentedRowEchelon():


def inverse():


def transpose():


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

