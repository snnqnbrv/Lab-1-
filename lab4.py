massiv = [12, 7, 5, 3, 8, 10, 6, 9]
with open("ilk_fayl.txt", "w") as file:
    for eded in massiv:
        file.write(str(eded) + "\n")

with open("ilk_fayl.txt", "r") as file:
    ededler = [int(satir.strip()) for satir in file.readlines()[:5]]

cem = sum(ededler)
with open("yeni_fayl.txt", "w") as file:
    for eded in ededler:
        file.write(str(eded) + "\n")
    file.write("Cəm:" + str(cem))

print("İlk 5 ədəd yeni fayla yazıldı və cəmi:", cem)
