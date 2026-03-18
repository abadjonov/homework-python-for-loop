total = 0

for i in range(1, 5+1):
    total += int(input(f'{i} talabaning yoshi: '))
avg = round(total/5, 1)
print(avg)