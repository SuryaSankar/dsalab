from typing import List

def count_distinct_windows(arr: List, k: int) -> int:
    left_ptr = 0
    right_ptr = k - 1
    counts = []
    while right_ptr < len(arr):
        elems = arr[left_ptr: right_ptr + 1]
        counts.append(len(set(elems)))
        left_ptr += 1
        right_ptr += 1
    return counts

if __name__ == '__main__':
    assert(count_distinct_windows([1, 2, 1, 3, 4, 2, 3], 4) == [3, 4, 4, 3])
    assert(count_distinct_windows([1, 2, 4, 4], 2) == [2, 2, 1])
    print("All cases passed successfully.")

