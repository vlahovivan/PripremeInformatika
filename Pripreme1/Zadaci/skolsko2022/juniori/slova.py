# Zadatak Slova
# Školsko natjecanje iz informatike 2022.
# Kategorija Juniori

m, n = [int(x) for x in input().split()]

# 2D lista slova
slova = [list(input()) for i in range(m)]

while len(slova) > 0:
    for c in slova[0]:
        print(c, end="")

    slova.pop(0)
    m = m-1

    slova = [[slova[i][n-j-1] for i in range(m)] for j in range(n)]

    n, m = m, n