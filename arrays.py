new_arr: list[int] = [1, 2, 3]
result: int = new_arr[0]

if 1 in new_arr:
    print(True)

for n in new_arr:
    if n == 1:
        print(True)
        break
# These are both linear search
