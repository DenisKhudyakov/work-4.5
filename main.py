# Задача №1
print('На улице идёт дождь?')
weather = int(input('Введите число: '))
if weather == 1:
    print('Пошел дождь. Возьмите зонтик')
elif weather == 0:
    print('Дождя нет')
else:
    print('Что-то пошло не так')
print('')
#Задача №2
rus_language = int(input('Введите количетсов балло по русскому языку: '))
math_les = int(input('Введите количетсов баллов по математик: '))
informatics = int(input('Введите количетсов баллов по информатике: '))
result = rus_language + math_les + informatics
if result >= 270:
    print('поздравляем вы поступили на бюджет')
else:
    print('к сожалению ты не прошел на бюджет')
print('')
#Задачка №3
calendar_day = int(input('Какое1 сегодня число? '))
if calendar_day <=31 and calendar_day % 2 == 0:
    print('ИДИ РАБОТАЙ')
elif calendar_day > 31:
    print('веден не корректная дата')
else:
    print('Можешь отдыхать')
print('')
#Задачка №4
chair1 = int(input('Введите цену стула: '))
chair2 = int(input('Введите цену стула: '))
chair3 = int(input('Введите цену стула: '))
sum_price = chair1 + chair3 + chair2
if sum_price > 10000:
    sum_price = sum_price - sum_price * 0.1
    print('Стоимость со скидкой', sum_price)
else:
    print('К оплате:', sum_price)
print('')
# Задачка №5
x = int(input('ведите число Х: '))
if x < 0:
    print('Введен', x, 'ответ', -1 * x)
else:
    print('Введен', x, 'ответ', x)
print('')
# Задачка №6
number_Kostya = int(input('Игрок введите Ваше число: '))
number_owner = int(input('Владелец введите Ваше число: '))
if number_Kostya >= number_owner:
    print('Итог:', number_Kostya - number_owner)
    print('Владелец платит')
    print('Конец игры')
else:
    print('Сумма:', number_owner + number_Kostya)
print('')
# Задачка №7
hours = int(input('Введите количество отработанных часов: '))
credit = int(input('Введите остаток по кредиту: '))
spending_on_food = int(input('ведите траты на еду: '))
salary = ((200 * hours) / (2 ** 3)) + hours
if salary >= credit + spending_on_food:
    print('Часов хватает! Можно отдохнуть')
else:
    print('Часов не хватает нужно работать больше')
print('')
# Задачка №8
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
max = 0

if number1 > number2:
    max = number1
    print('Максимальное число', max)
elif number3 > number1:
    max = number3
    print('Максимальное число', max)
else:
    max = number2
    print('Максимальное число', max)
