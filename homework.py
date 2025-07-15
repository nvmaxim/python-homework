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
