while True:
    try:
        rows = int(input("請輸入行數："))
        break
    except ValueError:
        print("輸入有誤，請重新輸入。")

# 正三角
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

# 逆三角
for i in range(rows, 0,-1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

# 左上直角三角形
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end="")
    for k in range(0, i):
        print("*", end="")
    print()

# 右上直角三角形
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(" ", end="")
    for k in range(0, i):
        print("*", end="")
    print()

# 右下直角三角形
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print("x", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

# 左下直角三角形
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, rows - i + 1):
        print(" ", end="")
    print()
