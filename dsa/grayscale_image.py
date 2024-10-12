from array_2d import Array2D

class GrayscaleImage:

    def __init__(self, numRows, numCols):
        self._image = Array2D(numRows, numCols)
        self._image.clear(0)
    
    def width(self):
        return self._image.numCols()
    
    def height(self):
        return self._image.numRows()
    
    def clamp(self, value):
        return max(0, min(value, 255))
    
    def clear(self, value):
        self._image.clear(self.clamp(value))
    
    def __getitem__(self, ndxTuple):
        return self._image[ndxTuple]
    
    def __setitem__(self, ndxTuple, value):
        self._image[ndxTuple] = self.clamp(value)
    
    def __str__(self):
        result = ""
        for i in range(self.height()):
            for j in range(self.width()):
                result += str(self._image[i, j]) + " "
            result += "\n"
        return result