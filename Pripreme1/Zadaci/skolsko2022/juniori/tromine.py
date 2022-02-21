# Zadatak Tromine
# Školsko natjecanje iz informatike 2022.
# Kategorija Juniori

r, s = [int(x) for x in input().split()]

matrica = [input() for i in range(r)]
memo = [[-1 for i in range(21)] for j in range(21)]


def provjeri(red, stupac):
    if stupac == s:
        return True

    if memo[red][stupac] != -1:
        return bool(memo[red][stupac])

    res = False


    stupac_set = {matrica[red + i][stupac] for i in range(3)}
    if len(stupac_set) == 3:
        res = res or provjeri(red, stupac + 1)

    tri_horizontalno = True

    if stupac + 2 < s:
        for i in range(3):
            red_set = {matrica[red + i][stupac + j] for j in range(3)}
            tri_horizontalno = tri_horizontalno and (len(red_set) == 3)

        if tri_horizontalno:
            res = res or provjeri(red, stupac + 3)
    
    memo[red][stupac] = res
    return memo[red][stupac]

rezultat = 0
for i in range(r-2):
    if provjeri(i, 0):
        rezultat += 1

print(rezultat)