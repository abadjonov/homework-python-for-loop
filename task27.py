n = int(input("Mahsulotlar sonini kiriting: "))

total = 0

for i in range(n):
    narx = float(input(f"{i+1}-mahsulot narxi: "))
    chegirma = narx * 0.9
    total += chegirma

print(total)