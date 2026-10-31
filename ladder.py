import math

n_values = [1, 10, 100, 1000]
print("n\tO(1)\tO(log n)\tO(n)\tO(n^2)")
for n in n_values:
    o1 = 1
    ologn = round(math.log2(n), 2) if n > 0 else 0
    on = n
    on2 = n ** 2
    print(f"{n}\t{o1}\t{ologn}\t{on}\t{on2}")
