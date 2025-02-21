class operations: 
    # elementary operations!
    # op1: multiply any equation by non-zero scalar on both sides
    def rowMult(matrix, row, scalar): 
        matrix[row] = matrix[row] * scalar
        return matrix

    # op2: multiply an equation by a scalar and add to another equation
    def rowAdd(matrix, targetRow, sourceRow, scalar):
        matrix[targetRow] = matrix[sourceRow] * scalar + matrix[targetRow]
        return matrix

    # use op1 and op2 in funcs below
    def rowEchelon(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        pivotRow = 0
        pivotCol = 0

        while pivotRow < rows and pivotCol < cols:
            # if pivot = zero skip the column
            if matrix[pivotRow][pivotCol] == 0:
                pivotCol += 1
                continue

            # if not already there make the pivot
            pivotValue = matrix[pivotRow][pivotCol]
            if pivotValue != 1:
                matrix = operations.rowMult(matrix, pivotRow, 1 / pivotValue)

            # make everything below the pivot 0
            for i in range(pivotRow + 1, rows):
                if matrix[i][pivotCol] != 0:
                    scalar = -matrix[i][pivotCol]
                    matrix = operations.rowAdd(matrix, i, pivotRow, scalar)

            # move to the next row and column
            pivotRow += 1
            pivotCol += 1
            
        return matrix

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

