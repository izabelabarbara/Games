import random
from tabulate import tabulate

numbers = []
  
def generateNumber():
  number = random.randint(0,90)
  return number
    
while len(numbers) < 8:
  number = generateNumber()
  if number not in numbers:
    numbers.append(number)

numbers.sort()
print (numbers)

bingo = [['','',''], ['','Bingo',''], ['','','']]
occupied_positions = [(1, 1)] # "Bingo" position
  
while len(occupied_positions)-1 < 8:
  for i in range (0,3): #row
      for j in range (0,3): #col
        row = i 
        col = j
        if (row, col) not in occupied_positions:
          occupied_positions.append((row,col))
          bingo[row][col]=numbers[len(occupied_positions)-2]


print(tabulate(bingo, colalign=('center', 'center', 'center'), tablefmt='fancy_grid'))

counter = 0 

while True:
  guess = int(input("Give me a number > "))  # Convert input to int
  for i in range(0,3):
      for j in range(0,3):
          if bingo[i][j] == guess:
              bingo[i][j] = "X"
              counter += 1
              print(tabulate(bingo, colalign=('center', 'center', 'center'), tablefmt='fancy_grid'))
              break
      else:  # This 'else' corresponds to the 'for', not the 'if'
          continue  # Continue if the inner loop wasn't broken
      break  # Inner loop was broken, break the outer loop
  else:  # This 'else' corresponds to the 'for', not the 'if'
      print(tabulate(bingo, colalign=('center', 'center', 'center'), tablefmt='fancy_grid'))
  if counter == 8:
    print()
    print("You win!")
    break