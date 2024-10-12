from typing import List

def bubble_sort(lst: List):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    print("All test cases passed successfully.")

if __name__ == "__main__":
    test_bubble_sort()