# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = [1, 2, 3, 4, 5, 6]
b = ['Hello', 'Git']
c = 'random text'

print(a, b, c)

string1 = input('Введите имя: ')
string2 = input('Введите ваш город: ')
age = int(input('Введите возраст: '))
favorite_number = int(input('Введите ваше любимое число: '))

print(string1, string2, age, favorite_number)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))
nn = int(10)
nnn = int(100)
summa = n + nn + nnn
print(summa)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

Number = int(input('Введите целое число: '))
N = []
while Number > 10:
    N.append(Number % 10)
    Number //=10
q = max(N)
print(q)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

v = float(input('Введите значение выручки: '))
i = float(input('Введите значение издержек: '))

if v > i:
  p = v - i
  r = p / v
  print(f'Ваша прибыль составила: {r}')
  w = int(input('Введите количество сотрудников: '))
  print(f'Рентабельность на 1 сотрудника: {p / w} ')
elif v == i:
    print('Нет прибыли')
else:
    print('Фирма работает в убыток')

# на шестую задачу у меня к сожалению не хватает времени, сдам её к следующему уроку