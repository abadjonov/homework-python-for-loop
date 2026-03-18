talaba = 5

yuqori = 0
past = 101 

for i in range(talaba):
    ball = int(input(f"{i+1}-talabaning ballini kiriting: "))
    
    if i == 0:
        yuqori = ball
        past = ball
    else:
        if ball > yuqori:
            yuqori = ball
        if ball < past:
            past = ball

print(f"Eng yuqori: {yuqori}, Eng past: {past}")