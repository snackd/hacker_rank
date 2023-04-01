while True:
    num = input("請輸入正整數：")
    try:
        num = int(num)
        if num <= 0:
            raise ValueError("輸入的數字不是正整數")
        break
    except ValueError as e:
        print("輸入的不是正整數，請重新輸入。")

is_prime = True
if num == 1:
    is_prime = False
elif num > 1:
    for i in range(2, num):
        if (num % i == 0):
            is_prime = False
            break

print(is_prime)

q = deque([1, 2, 3])
