# git remote set-url origin https://github.com/nvmaxim/python-homework.git
# git push -u origin main
# git pull origin main --allow-unrelated-histories
# git push -u origin main


a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)

# ========================================#
x = int(input())

if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")

# ============================================#

a = int(input())
b = int(input())
operation = input()

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        result = "На ноль делить нельзя!"
    else:
        result = a / b
else:
    result = "Неверная операция"

print(result)

# ============================================#

color1 = input().lower()  # Приводим ввод к нижнему регистру для удобства
color2 = input().lower()

primary_colors = {"красный", "синий", "желтый"}  # Множество основных цветов

if color1 not in primary_colors or color2 not in primary_colors:
    print("ошибка цвета")
else:
    if color1 == color2:
        print(color1)  # Если цвета одинаковые, результат тот же цвет
    elif {color1, color2} == {"красный", "синий"}:
        print("фиолетовый")
    elif {color1, color2} == {"красный", "желтый"}:
        print("оранжевый")
    elif {color1, color2} == {"синий", "желтый"}:
        print("зеленый")


n = int(input())

if n % 100 == 0:
    print("YES")
else:
    print("NO")


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
sum = x1 + y1 + x2 + y2
if sum % 2 == 0:
    print("YES")
else:
    print("NO")
