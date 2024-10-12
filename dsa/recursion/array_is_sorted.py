def check_is_sorted(arr):
    if len(arr) == 1:
        return True
    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return False
    return check_is_sorted(arr[:len(arr) - 1])

if __name__ == '__main__':
    print(check_is_sorted([1, 2, 3, 4, 5])) # True
    print(check_is_sorted([1, 2, 3, 5, 4])) # False
    print(check_is_sorted([1])) # True
    print(check_is_sorted([5, 4, 3, 2, 1])) # False
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])) # True
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 9, 8])) # False
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 10, 9])) # False
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # True
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10])) # False
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # True
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11])) # False
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # True
    print(check_is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12])) # False
