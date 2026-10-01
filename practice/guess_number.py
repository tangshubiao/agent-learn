import random

secret = random.randint(1, 100)
print("我想了一个 1 到 100 的数")


count = 0
while True:
    guess = int(input("你猜是多少？"))
    count = count + 1

    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"猜中了！你一共猜了 {count} 次")
        break