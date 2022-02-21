# Zadatak PVC
# Školsko natjecanje iz informatike 2022.
# Kategorija Juniori

n = int(input())

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

tipovi = input()

for i in range(4):
    for tip in tipovi:
        print(prozori[ord(tip) - ord('A')][i], end="")
    print("")
