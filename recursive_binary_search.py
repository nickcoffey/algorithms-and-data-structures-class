def recursive_binary_search(arr: list[int], target: int) -> bool:
    if len(arr) == 0:
        return False

    midpoint: int = len(arr) // 2
    if arr[midpoint] == target:
        return True
    if arr[midpoint] < target:
        return recursive_binary_search(arr[midpoint + 1 :], target)
    if arr[midpoint] > target:
        return recursive_binary_search(arr[:midpoint], target)


def verify(result: bool):
    print(f"Target found: {result}")


numbers: list[int] = list(range(1, 10))
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
