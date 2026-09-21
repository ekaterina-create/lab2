print('1 - Километры')
print('2 - Метры')
print('3 - Сантиметры')
print('4 - Миллиметры')
print('5 - Мили')
print('6 - Ярды')

a = int(input('Из какой единицы переводим: '))
b = int(input('В какую единицу переводим: '))
x = float(input('Введите значение: '))

if a == 1 and b == 2:
    x = x * 1000

elif a == 2 and b == 1:
    x = x / 1000

elif a == 1 and b == 3:
    x = x * 100000

elif a == 3 and b == 1:
    x = x / 100000

elif a == 1 and b == 4:
    x = x * 1000000

elif a == 4 and b == 1:
    x = x / 1000000

elif a == 1 and b == 5:
    x = x / 1.609344

elif a == 5 and b == 1:
    x = x * 1.609344

elif a == 1 and b == 6:
    x = x * 1093.6133

elif a == 6 and b == 1:
    x = x / 1093.6133

elif a == 2 and b == 3:
    x = x * 100

elif a == 3 and b == 2:
    x = x / 100

elif a == 2 and b == 4:
    x = x * 1000

elif a == 4 and b == 2:
    x = x / 1000

elif a == 2 and b == 5:
    x = x / 1609.344

elif a == 5 and b == 2:
    x = x * 1609.344

elif a == 2 and b == 6:
    x = x * 1.0936133

elif a == 6 and b == 2:
    x = x / 1.0936133

elif a == 3 and b == 4:
    x = x * 10

elif a == 4 and b == 3:
    x = x / 10

elif a == 3 and b == 5:
    x = x / 160934.4

elif a == 5 and b == 3:
    x = x * 160934.4

elif a == 3 and b == 6:
    x = x / 91.44

elif a == 6 and b == 3:
    x = x * 91.44

elif a == 4 and b == 5:
    x = x / 1609344

elif a == 5 and b == 4:
    x = x * 1609344

elif a == 4 and b == 6:
    x = x / 914.4

elif a == 6 and b == 4:
    x = x * 914.4

elif a == 5 and b == 6:
    x = x * 1760

elif a == 6 and b == 5:
    x = x / 1760

print(f'Результат: {x:.2f}')