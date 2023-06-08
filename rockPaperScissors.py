print ('''\033[35mE P I C  🪨  📄 ✂️   B A T T L E

Select your move (R, P or S)
''')

max = int(input('Till how many points are we playing? '))
print ()
print ('OK, let\'s go!!')
print ()

from getpass import getpass as input

score1 = 0
score2 = 0

while score1 < max and score2 < max:

  p1 = input ('Player 1 > ')
  p2 = input ('Player 2 > ')

  if p1 == 'R' or p1 == 'r':
    if p2 == 'R' or p2 == 'r':
      print ('Boring! No winners... Try again!')
    elif p2 == 'P' or p2 == 'p':
      print ('Player 2 wins!')
      score2 += 1
    elif p2 == 'S' or p2 == 's':
      print ('Player 1 wins!')
      score1 += 1


  elif p1 == 'P' or p1 == 'p':
    if p2 == 'R' or p2 == 'r':
      print ('Player 1 wins!')
      score1 += 1
    elif p2 == 'P' or p2 == 'p':
      print ('Boring! No winners... Try again!')
    elif p2 == 'S' or p2 == 's':
      print ('Player 2 wins!')
      score2 += 1

  
  elif p1 == 'S' or p1 == 's':
    if p2 == 'R' or p2 == 'r':
      print ('Player 2 wins!')
      score2 += 1
    elif p2 == 'P' or p2 == 'p':
      print ('Player 1 wins!')
      score1 += 1
    elif p2 == 'S' or p2 == 's':
      print ('Boring! No winners... Try again!')
      
  print ()


if score1 > score2:
  print ('Player 1 is the greatest champion!')
elif score2 > score1:
  print ('Player 2 is the greatest champion!')
else:
  print ('It\'s hard to tell if we have a winner...')