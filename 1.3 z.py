year = int(input('Введите год: '))

leap = False

if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True

if leap:
    print(year, 'является високосным годом')
else:
    print(year, 'не является високосным годом')