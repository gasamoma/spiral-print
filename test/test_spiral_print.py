from src.spiral_print import print_spiral
answer_ten="1 2 3 4 5 6 7 8 9 20 30 40 50 60 70 80 90 100 99 98 97 96 95 94 93 92 81 71 61 51 41 31 21 11 12 13 14 15 " \
           "16 17 18 29 39 49 59 69 79 89 88 87 86 85 84 83 72 62 52 42 32 22 23 24 25 26 27 38 48 58 68 78 77 76 75 74 63 53 43 33 " \
           "34 35 36 47 57 67 66 65 54 44 45 56 "


def test_sprint_spiral():
    matriz=[]
    for x in range(1,11):
        newitem=[]
        for y in range(10):
            newitem.append((x + (y * 10)))
        matriz.append(newitem)
    assert answer_ten == print_spiral(matriz)