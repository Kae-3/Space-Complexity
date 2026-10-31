def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    checks = 0
    while low <= high:
        checks += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, checks
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, checks

sizes = [10, 100, 1000, 10000]
for size in sizes:
    arr = list(range(size))
    target = size - 1
    index, checks = binary_search(arr, target)
    print(f"Size: {size}, Checks: {checks}")