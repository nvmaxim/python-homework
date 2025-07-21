n = int(input())

if n % 2 != 0:  # Если число нечетное
    print("YES")
else:  # Все четные числа
    if 2 <= n <= 5:
        print("NO")
    elif 6 <= n <= 20:
        print("YES")
    else:  # Все четные числа > 20
        print("NO")
