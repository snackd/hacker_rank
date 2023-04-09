def f(a, b):
    # 如果相除餘數為 0，回傳結果
    if a % b == 0:
        return b
    # 如果相除不為 0，表示還沒找到最大公因數
    else:
        return f(b, a % b)


print(f(120, 24))
