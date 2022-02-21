# Zadatak Domine
# Školsko natjecanje iz informatike 2022.
# Kategorija Seniori

r, s = [int(x) for x in input().split()]

matrica = [input() for i in range(r)]
memo = [[-1 for i in range(21)] for j in range(21)]


def provjeri(red, stupac):
    if stupac == s:
        return True

    if memo[red][stupac] != -1:
        return bool(memo[red][stupac])

    res = False

    stupac_set = {matrica[red + i][stupac] for i in range(2)}
    if len(stupac_set) == 2:
        res = res or provjeri(red, stupac + 1)

    dva_horizontalno = True

    if stupac + 1 < s:
        for i in range(2):
            red_set = {matrica[red + i][stupac + j] for j in range(2)}
            dva_horizontalno = dva_horizontalno and (len(red_set) == 2)

        if dva_horizontalno:
            res = res or provjeri(red, stupac + 2)
    
    memo[red][stupac] = res
    return memo[red][stupac]

rezultat = 0
for i in range(r-1):
    if provjeri(i, 0):
        rezultat += 1

print(rezultat)