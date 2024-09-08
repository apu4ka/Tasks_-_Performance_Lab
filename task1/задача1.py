#import sys

n = int(input()) # значения вводимых  n и m 
m = int(input())

numbers = [] # Создаем массив чисел от 1 до n
for i in range(1, n + 1):
  numbers.append(i)

way = []  # Список для слздания пути


for i in range(n):
  first_interval = (i * (m - 1)) % n # Вычисляем начало интервала (с учетом цикличности)
  interval = numbers[first_interval: first_interval + m]# Выбираем интервал длины m
  way.append(interval[0]) # Добавляем первый элемент интервала в путь
  
  if interval[-1] == numbers[0]:# Конец интервала равен началу массива?
    way.insert(0, numbers[0]) 
    break # Если да, выходим из цикла

print("Путь:", *way)# Выводим путь

