# Zadatak Spirala
# Školsko natjecanje iz informatike 2022.
# Kategorija Seniori

r, s = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]

rezultat = 0
prijenos = 0

while not (r == 0 or s==0):
    res = 0

    if x == 1:
        res = (s * (s+1)) // 2 + s * prijenos
    elif y >= 1 and y <= s:
        res = y + prijenos

    r, s, x, y, prijenos = s, r-1, s-y+1, x-1, prijenos + s
    rezultat += res

print(rezultat)