x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

# Проверка хода по горизонтали или вертикали
if x1 == x2 or y1 == y2:
    print("YES")
# Проверка хода по диагонали
elif abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

123
