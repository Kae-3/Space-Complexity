def countdown(n, call_count=0):
    call_count += 1
    print(f"Call {call_count}: n = {n}")
    if n <= 0:
        return call_count
    return countdown(n - 1, call_count)

total_calls = countdown(5)
print(f"Total calls: {total_calls}")