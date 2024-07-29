from typing import Optional


def binary_search(arr: list[int], target: int):
    first: int = 0
    last: int = len(arr) - 1

    while first <= last:
        midpoint: int = (first + last) // 2  # // is floor division
        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] < target:
            first = midpoint + 1
        else:  # arr[midpoint] > target
            last = midpoint - 1

    return None


def verify(index: Optional[int]):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers: list[int] = list(range(1, 10))
result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
