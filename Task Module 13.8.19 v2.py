try:
    kolBil = int(input('Сколько билетов желаете приобрести? >'))
    agePos = (input('Сколько лет каждому посетителю?(через пробел) >')).split()
    disc = 1
    S = 0
    if len(agePos) != kolBil:
        raise ValueError("!Перечислены возрасты не всех участников!")
except ValueError as error:
    print(error)
    print('!Либо введено больше значений, чем ожидается!')
else:
    if kolBil > 3:
        disc = kolBil*90/100  # 10% скидка от 4-х и более персон
    # 3 или 5
    # 14 19 30 или 11 18 25 26 255
    for age in agePos:
        if int(age) < 18:
            print(f'{age}, значит... Вам нет 18-ти - Проходите бесплатно!')
        elif 18 <= int(age) <= 25:
            price = disc*990
            S += price
            print(f'Стоимость для {age}-летнего посетителя ={price} руб.')
        else:
            price = disc*1390
            S += price
            print(f'Стоимость для {age}-летнего посетителя ={price} руб.')
    print('-------------------------------------------------')
    print(f'Общая сумма для оплаты:\n\t\t ={S} руб.')
