import random
MIN = 1
MAX = 45
COUNT = 6

quick_picks = int(input("Enter number of quick picks: "))

for i in range(quick_picks):
    pick = []
    while len(pick) < COUNT:
        num = random.randint(MIN, MAX)
        if num not in pick:
            pick.append(num)

    pick.sort()

    print(" ".join([f"{n:2}" for n in pick]))
