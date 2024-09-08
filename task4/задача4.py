import sys


file_path = input("Введите путь к файлу: ")  # Ввод пути 

nums = []

with open(file_path, 'r') as f:
    for line in f:
        nums.append(int(line.strip()))

# Сортируем массив для поиска медианы
nums.sort()
median = nums[len(nums) // 2]

# Считаем количество ходов
count = 0
for num in nums:
    count += abs(num - median)

print(count) 