import random

tahta = [["___", "___", "___"],
["___", "___", "___"],
["___", "___", "___"]]

kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

x_durum = []
o_durum = []
kazanma_olcutleri.sort()


sira = 1
while True:

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 2)

    if sira % 2 == 0:
        isaret = "X".center(3)
    else:
        isaret = "O".center(3)

    print("Oyun sirasi: {}\n".format(isaret))

    x = input("Soldan saga [1, 2, 3]: ".ljust(30))
    try:
        x = int(x)
    except ValueError:
        print("Hatali giris yapildi...")
        continue
    if x > 3 or x < 1:
        print("Hatali giris yaptiniz...")
        continue

    y = input("Yukardan asagi [1, 2, 3]".ljust(30))
    try:
        y = int(y)
    except ValueError:
        print("Hatali giris yapildi...")
        continue
    if y > 3 or y < 1:
        print("Hatali giris yaptiniz...")
        continue

    x -= 1                #python siraya 0 dan basladigi icin -1 ekliyoruz ki 1 girince 0 anlasin
    y -= 1

    if tahta[y][x] == "___":
        tahta[y][x] = isaret
        sira += 1
        if isaret == "X".center(3):
            x_durum += [[y, x]]
        elif isaret == "O".center(3):
            o_durum += [[y, x]]

    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")

    x_durum.sort()
    o_durum.sort()
    for i in kazanma_olcutleri:                         # kimin kazandigini belirleme
        if x_durum == i:
            print("Tebrikler 'X' kazandi")
            quit()
        elif o_durum == i:
            print("Tebrikler 'O' kazandi")
            quit()

