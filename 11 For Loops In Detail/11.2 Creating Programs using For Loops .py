# ====================== Creating table =====================
'''table = int(input('Which Table Should I Print For You? '))
table_range = int(input('What Should Be the Range Of The Table? '))
for x in range(1, table_range+1):
    print(table, ' x ', x, ' = ', table*x)
print('Finished Printing Your Table!!')'''

# ======================= Rolling Dice ============================
import random
from typing_extensions import Self
rolling_dice_list = [1, 2, 3, 4, 5, 6]
name = str(input('Enter Your Name: '))
start = str(input(
    'Do You Want To Start Rolling The Dice?\n[y] = yes (or) [n] = no\nChoice: '))
myRange = int(input('Number of Rolls: '))
P1 = []
P2 = []
for i in range(0, myRange):
    while start == 'y':
        Player1 = random.choice(rolling_dice_list)
        Player2 = random.choice(rolling_dice_list)
        results = f'{Player1} & {Player2}'
        print(results)
        break
    P1.append(Player1)
    P2.append(Player2)
print(P1)
print(P2)
