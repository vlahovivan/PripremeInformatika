# Zadatak Prozori
# Školsko natjecanje iz informatike 2022.
# Kategorija Seniori

m, n = [int(x) for x in input().split()]

prozori = [
    [
        '....',
        '....',
        '....',
        '....'
    ],
    [
        '####',
        '#..#',
        '#..#',
        '####'
    ],
    [
        '....',
        '.##.',
        '.##.',
        '....'
    ],
    [
        '####',
        '####',
        '####',
        '####'
    ]
]

tipovi = [input() for i in range(m)]


for redak in tipovi:
    for i in range(4):
        for tip in redak:
            print(prozori[ord(tip) - ord('A')][i], end="")
        print("")
