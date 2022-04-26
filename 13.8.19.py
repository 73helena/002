t = int(input("Введите кол-во билетов? "))
print("Укажите возраст каждого посетителя")
s = 0
for i in range(t):
    age = int(input("Возраст: "))
    if age < 18:
        s= s + 0
    elif 18 <= age < 25:
        s = s + 990
    else:
        s= s + 1390
if t > 3:
    f = 0.9
else:
    f = 1
print("К оплате :", s * f)
