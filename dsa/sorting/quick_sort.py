from typing import List

def quick_sort(lst: List):
    def partition(left, right):
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i+1], lst[right] = lst[right], lst[i+1]
        return i+1

    def sort(left, right):
        if left < right:
            pi = partition(left, right)
            sort(left, pi-1)
            sort(pi+1, right)

    sort(0, len(lst)-1)
    return lst

def test_quick_sort():
    assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert quick_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    print("All test cases passed successfully.")

if __name__ == "__main__":
    test_quick_sort()