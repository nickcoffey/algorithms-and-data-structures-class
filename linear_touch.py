from typing import Optional


def linear_search(arr: list[int], target: int):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None


def verify(index: Optional[int]):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers: list[int] = list(range(1, 10))
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
