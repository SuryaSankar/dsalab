from array import Array

class Vector:
    def __init__(self):
        self._theElements = Array(2)
        self._size = 0
        self._capacity = 2
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        print(f"Index {index}")
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._theElements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._theElements[index] = value
    
    def _resize(self, new_capacity):
        new_elements = Array(new_capacity)
        for i in range(self._size):
            new_elements[i] = self._theElements[i]
        self._theElements = new_elements
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._theElements[self._size] = value
        self._size += 1
    
    def insert(self, index, value):
        assert index >= 0 and index <= len(self), "Array subscript out of range"
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._theElements[i] = self._theElements[i-1]
        self._theElements[index] = value
        self._size += 1
    
    def remove(self, value):
        for i in range(self._size):
            if self._theElements[i] == value:
                for j in range(i, self._size-1):
                    self._theElements[j] = self._theElements[j+1]
                self._size -= 1
                if self._size < self._capacity // 4:
                    self._resize(self._capacity // 2)
                return
        raise ValueError("Value not found")
    
    def __str__(self):
        result = ""
        for i in range(self._size):
            result += str(self._theElements[i]) + " "
        return result
    
    def __iter__(self):
        for i in range(self._size):
            yield self._theElements[i]
    
if __name__ == '__main__':
    vec = Vector()
    vec.append(1)
    vec.append(2)
    vec.append(3)
    vec.append(4)
    vec.append(5)
    print(vec)
    vec.insert(2, 6)
    print(vec)
    vec.remove(3)
    print(vec)
    vec.remove(1)
    print(vec)
    vec.remove(5)
    print(vec)
    vec.remove(4)
    print(vec)
    for elem in vec:
        print(elem)
    

