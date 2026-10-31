def formula_approach(n):
    return n * (n + 1) // 2

def loop_approach(n):
    total = 0
    steps = 0
    for i in range(1, n + 1):
        total += i
        steps += 1
    return total, steps

def nested_loop_approach(n):
    total = 0
    steps = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total += 1
            steps += 1
    return total, steps

n = 5
print(formula_approach(n))
print(loop_approach(n))
print(nested_loop_approach(n))