n = int(input("Savdo nuqtalari sonini kiriting: "))
total = 0 

for i in range(n):
    daromad = float(input(f"{i+1}-savdo nuqtasi daromadi: "))
    total += daromad

ortacha_daromad = total / n

print(ortacha_daromad)