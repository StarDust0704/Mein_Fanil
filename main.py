# 1ist progran
# Возводим число 9 в степень 0.5 (это эквивалентно извлечению квадратного корня)
result = 9 ** 0.5

# Умножаем полученный результат на 5
final_result = result * 5

# Выводим итоговый результат в консоль
print(final_result)

# 2nd program
# Проверка условий
condition_1 = 9.99 > 9.98
condition_2 = 1000 != 1000.1

# Логическое объединение условий
result = condition_1 and condition_2

# Вывод результата в консоль
print(result)

# 3rd program

# Вычисляем выражение без приоритета
result_without_priority = 2 * 2 + 2
print(f'Без приоритета: {result_without_priority}')

# Вычисляем выражение с приоритетом для сложения
result_with_addition_priority = 2 * (2 + 2)
print(f'С приоритетом для сложения: {result_with_addition_priority}')

# Сравниваем результаты
comparison_result = result_without_priority == result_with_addition_priority
print(f'Результаты равны: {comparison_result}')

# 4th program
# Исходная строка
s = '123.456'

# Преобразуем строку в число с плавающей точкой
number = float(s)

# Умножаем на 10
multiplied_number = number * 10

# Берём целую часть от произведения
integer_part = int(multiplied_number)

# Берём последнюю цифру целой части
first_digit_after_decimal = integer_part % 10

# Выводим результат
print(first_digit_after_decimal)






