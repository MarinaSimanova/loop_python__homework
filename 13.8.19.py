number_of_tickets = int(input("Введите количество билетов: "))
age = [int(input("Введите ваш возраст: ")) for i in range(number_of_tickets)]
sum1 = 0
sum2 = 0
for i in age:
    if 0 <= i < 18:
        sum1 += 0
    elif 18 <= i < 25:
        sum1 += 990
    elif 25 <= i < 150:
        sum1 += 1390
    else:
        raise ValueError("Введён неверный формат данных.")
if number_of_tickets > 3:
    sum2 = round((sum1 / 100) * 90)
    print("Сумма к оплате со скидкой: ", sum2)
else:
    print("Сумма к оплате: ", sum1)
