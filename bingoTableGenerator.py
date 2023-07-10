import random
from tabulate import tabulate

numbers = []

def generateNumber():
  number = random.randint(0,90)
  return number

# creating a list
while len(numbers) < 8:
  number = generateNumber()
  if number not in numbers:
    numbers.append(number)

numbers.sort()

# just to check. Delete it later

# assigning list places to table places

bingo = [[None,None,None],[None,"Bingo",None],[None,None,None]]

bingo[0][0]=numbers[0]
bingo[0][1]=numbers[1]
bingo[0][2]=numbers[2]
bingo[1][0]=numbers[3]
bingo[1][2]=numbers[4]
bingo[2][0]=numbers[5]
bingo[2][1]=numbers[6]
bingo[2][2]=numbers[7]


print(tabulate(bingo, tablefmt='fancy_grid'))

# WITHOUT THE LIST

import random
from tabulate import tabulate

def generateNumber():
  return random.randint(0,90)

bingo = [[None,None,None], [None,"Bingo",None], [None,None,None]]

occupied_positions = [(1, 1)] # "Bingo" position

while len(occupied_positions) < 9:
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    if (row, col) not in occupied_positions:
        occupied_positions.append((row, col))
        bingo[row][col] = generateNumber()

print(tabulate(bingo, colalign=('center', 'center', 'center'),
tablefmt='fancy_grid'))
