def iterative_binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    checks = 0
    while low <= high:
        checks += 1
        mid = (low + high) // 2
        if seats[mid] == target:
            return mid, checks
        elif seats[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, checks

def recursive_binary_search(seats, target, low, high, checks=0):
    if low > high:
        return -1, checks
    checks += 1
    mid = (low + high) // 2
    if seats[mid] == target:
        return mid, checks
    elif seats[mid] < target:
        return recursive_binary_search(seats, target, mid + 1, high, checks)
    else:
        return recursive_binary_search(seats, target, low, mid - 1, checks)

seats = sorted([12, 25, 34, 45, 56, 67, 78, 89, 90])
target = 67
print(iterative_binary_search(seats, target))
print(recursive_binary_search(seats, target, 0, len(seats) - 1))