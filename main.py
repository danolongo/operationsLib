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

    def augmentedRowEchelon(matrix):
        matrix = operations.rowEchelon(matrix)

        rows = len(matrix)
        cols = len(matrix[0])

        # start from last row and move upwards and backwards
        for pivotRow in range(rows - 1, -1, -1):
            pivotCol = 0
            while pivotCol < cols - 1:  # exclude augmented column
                if matrix[pivotRow][pivotCol] == 1:
                    break
                pivotCol += 1

            # getting rid of zeroes above pivot
            for i in range(pivotRow - 1, -1, -1):  # iterate over the rows above current pivot row
                if matrix[i][pivotCol] != 0:
                    scalar = -matrix[i][pivotCol]
                    matrix = operations.rowAdd(matrix, i, pivotRow, scalar)

        return matrix

    def inverse(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        if rows != cols:
            raise ValueError("matrix must be square to find inverse")

        # augment the matrix with the identity matrix
        # [1 if i == j else 0 for j in range(rows)] adds the identity matrix row by row
        augMatrix = [row + [1 if i == j else 0 for j in range(rows)] for i, row in enumerate(matrix)]

        # apply rowEchelon to the augmented matrix
        augMatrix = operations.rowEchelon(augMatrix)

        # left side is now the identity matrix and the right side is the inverse
        # work backwards to make sure the augmented part has become the inverse
        inverseMatrix = augMatrix

        return [row[cols:] for row in inverseMatrix]  # Extract the right-hand side of the augmented matrix


    def transpose(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # create empty matrix with reversed dimensions
        result = [[0] * rows for i in range(cols)]

        # fill the result matrix with transposed values
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]

        return result


    def addMatrix(matrix1, matrix2):
        # if not tof the same dimensions raise error
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("matrices must be of the same size to add")

        # initialize result
        result = []

        # doing the addition element per element
        for i in range(len(matrix1)):
            row = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
            result.append(row)
        
        return result


    def subtractMatrix(matrix1, matrix2):
        # if not tof the same dimensions raise error
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("matrices must be of the same size to subtract")

        # initialize result
        result = []

        # doing the subtraction element per element
        for i in range(len(matrix1)):
            row = [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
            result.append(row)
        
        return result

    def matrixMult():

    def dotProd():
        

    def getDeterminant():

