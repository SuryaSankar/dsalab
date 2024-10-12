from array_2d import Array2D

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self._grid.clear(self.DEAD_CELL)

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList):
        for coord in coordList:
            self.set_cell(coord[0], coord[1])

    def is_live_cell(self, row, col):
        return self._grid[row, col] == self.LIVE_CELL

    def clear_cell(self, row, col):
        self._grid[row, col] = self.DEAD_CELL

    def set_cell(self, row, col):
        self._grid[row, col] = self.LIVE_CELL

    def num_live_neighbors(self, row, col):
        num_live_neighbors = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < self.numRows() and j >= 0 and j < self.numCols() and (i != row or j != col):
                    if self.is_live_cell(i, j):
                        num_live_neighbors += 1
        return num_live_neighbors

    def __str__(self):
        result = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if self.is_live_cell(i, j):
                    result += "*"
                else:
                    result += "."
            result += "\n"
        return result

    def update(self):
        live_cells = []
        dead_cells = []
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                num_live_neighbors = self.num_live_neighbors(i, j)
                if self.is_live_cell(i, j):
                    if num_live_neighbors < 2 or num_live_neighbors > 3:
                        dead_cells.append((i, j))
                else:
                    if num_live_neighbors == 3:
                        live_cells.append((i, j))
        for cell in live_cells:
            self.set_cell(cell[0], cell[1])
        for cell in dead_cells:
            self.clear_cell(cell[0], cell[1])