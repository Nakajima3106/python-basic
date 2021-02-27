import random
while True:
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    print(dice1, dice2)
    if dice1 == dice2:
        print("終了します")
        break