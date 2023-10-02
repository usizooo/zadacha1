a = int (input ("Введите первое число:"))
b = int (input ("Введите второе число:"))
c = int (input ("Введите третье число:"))
d = int (input ("Введите четвертое число:"))
numbers = [a, b, c, d]
numbers.sort()
num1 = numbers[0]
num2 = numbers[3]
print ("Минимальное значение:", num1, "Максимальное значение:", num2)