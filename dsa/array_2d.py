from array import Array

class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)
    
    def numRows(self):
        return len(self._theRows)
    
    def numCols(self):
        return len(self._theRows[0])
    
    def clear(self, value):
        for i in range(self.numRows()):
            self._theRows[i].clear(value)
    
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        return self._theRows[row][col]
    
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        self._theRows[row][col] = value

if __name__ == '__main__':
    arr = Array2D(3, 3)
    arr[0, 0] = 1
    arr[0, 1] = 2
    arr[0, 2] = 3
    arr[1, 0] = 4
    arr[1, 1] = 5
    arr[1, 2] = 6
    arr[2, 0] = 7
    arr[2, 1] = 8
    arr[2, 2] = 9
    for i in range(arr.numRows()):
        for j in range(arr.numCols()):
            print(arr[i, j], end=' ')
        print()
    arr.clear(None)
    for i in range(arr.numRows()):
        for j in range(arr.numCols()):
            print(arr[i, j], end=' ')
        print()