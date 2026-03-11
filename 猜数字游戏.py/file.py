import random
number = random.randint(1, 100)
guess = 0
count = 0

while guess != number:
    guess = int(input("请输入你要猜的数字(1-100)："))
    count += 1
    if guess < number:
        print("小了")
    elif guess > number:
        print("大了")
    else:
        print("恭喜你，猜对了！")
        print(f"你一共猜了{count}次")
        break