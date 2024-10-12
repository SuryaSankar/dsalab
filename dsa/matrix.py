from array_2d import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(None)
    
    def numRows(self):
        return self._theGrid.numRows()
    
    def numCols(self):
        return self._theGrid.numCols()
    
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple]
    
    def __setitem__(self, ndxTuple, value):
        self._theGrid[ndxTuple] = value

    def scale_by(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self[i, j] *= scalar

    def transpose(self):
        new_matrix = Matrix(self.numCols(), self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new_matrix[j, i] = self[i, j]
        return new_matrix
    
    def __add__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and self.numCols() == rhsMatrix.numCols(), "Matrix sizes not compatible for the operation"
        new_matrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new_matrix[i, j] = self[i, j] + rhsMatrix[i, j]
        return new_matrix
    
    def __sub__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and self.numCols() == rhsMatrix.numCols(), "Matrix sizes not compatible for the operation"
        new_matrix = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new_matrix[i, j] = self[i, j] - rhsMatrix[i, j]
        return new_matrix
    
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), "Matrix sizes not compatible for the operation"
        new_matrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(rhsMatrix.numCols()):
                for k in range(self.numCols()):
                    new_matrix[i, j] += self[i, k] * rhsMatrix[k, j]
        return new_matrix
    
    def __str__(self):
        result = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                result += str(self[i, j]) + " "
            result += "\n"
        return result
    
if __name__ == '__main__':
    mat1 = Matrix(2, 2)
    mat1[0, 0] = 1
    mat1[0, 1] = 2
    mat1[1, 0] = 3
    mat1[1, 1] = 4
    print(mat1)
    mat1.scale_by(2)
    print(mat1)
    mat2 = mat1.transpose()
    print(mat2)
    mat3 = mat1 + mat2
    print(mat3)
    mat4 = mat1 - mat2
    print(mat4)
    mat5 = mat1 * mat2
    print(mat5)
    mat6 = Matrix(2, 3)
    mat6[0, 0] = 1
    mat6[0, 1] = 2
    mat6[0, 2] = 3
    mat6[1, 0] = 4
    mat6[1, 1] = 5
    mat6[1, 2] = 6
    mat7 = Matrix(3, 2)
    mat7[0, 0] = 1
    mat7[0, 1] = 2
    mat7[1, 0] = 3
    mat7[1, 1] = 4
    mat7[2, 0] = 5
    mat7[2, 1] = 6
    mat8 = mat6 * mat7
    print(mat8)
    mat9 = Matrix(2, 2)
    mat9[0, 0] = 1
    mat9[0, 1] = 2
    mat9[1, 0] = 3
    mat9[1, 1] = 4
    print(mat9)
    mat10 = mat9 * mat9
    print(mat10)
    mat11 = Matrix(2, 2)
    mat11[0, 0] = 1
    mat11[0, 1] = 2
    mat11[1, 0] = 3
    mat11[1, 1] = 4
    print(mat11)
    mat12 = mat11 + mat11
    print(mat12)
