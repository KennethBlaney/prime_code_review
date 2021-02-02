a = 2
b = 100
i = a
a = 1
P = []
C = []
while i >= a and i <= b:
    print(i)
    import math
    j = 2
    p = "True"
    while j <= math.sqrt(i):
        if i == j:
            continue
        k = i/j
        if k == int(k):
            p = "False"
            break
        j = j + 1
    if p == "True":
        P.append(i)
    else:
        C.append(i)
    i = i + 1
print(P)
