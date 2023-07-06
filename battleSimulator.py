import random
import time
import os

listOfNames = ['Aspect', 'Kraken', 'Bender', 'Lynch', 'Big Papa', 'Mad Dog', 'Bowser', 'O\'Doyle', 'Bruise', 'Psycho', 'Cannon', 'Ranger', 'Clink', 'Ratchet', 'Cobra', 'Reaper', 'Colt', 'Rigs', 'Crank', 'Ripley', 'Creep', 'Roadkill', 'Daemon', 'Ronin', 'Decay', 'Rubble', 'Diablo', 'Sasquatch', 'Doom', 'Scar',]

listOfTypes = ['human', 'wizzard', 'elf', 'dog', 'plant', 'ogre', 'fairy', 'troll']

def generateName():
  n = random.randint(0,len(listOfNames)-1)
  name = listOfNames[n]
  return name

def generateType():
  m = random.randint(0,len(listOfTypes)-1)
  type = listOfTypes[m]
  return type

def generateSex():
  x = random.randint(0,2)
  if x == 0:
    sex = 'Her'
    return sex
  elif x == 1:
    sex = 'His'
    return sex
  else:
    sex = 'Their'
    return sex

def generateHealth():
  i = random.randint(1,6)
  j = random.randint(1,8)
  health = int((i*j)/2 + 10)
  return health

def generateStrength():
  i = random.randint(1,6)
  j = random.randint(1,8)
  strength = int((i*j)/2 + 10)
  return strength

def roll(x):
  x = random.randint(1,x)
  return x

  
print('BATTTLE TIME')
print()

firstChar = input ('Press enter to generate your character')
print()
if firstChar == '':
  time.sleep(1)
  name1 = generateName()
  type1 = generateType()
  sex1 = generateSex()
  health1 = generateHealth()
  strength1 = generateStrength()
  print (f'Your legend is {name1} the {type1}.')
  time.sleep(2)
  print(f'''{sex1} health is {health1}.
{sex1} strength is {strength1}.
''')

time.sleep(1)
print()

secondChar = input('Now press enter to generate your second character')
print ()
if secondChar == '':
  time.sleep(1)
  name2 = generateName()
  type2 = generateType()
  sex2 = generateSex()
  health2 = generateHealth()
  strength2= generateStrength()
  print (f'Your legend is {name2} the {type2}')
  time.sleep(2)
  print(f'''{sex2} health is {health2}.
{sex2} strength is {strength2}.
''')

damage = abs(strength2-strength1)+1

time.sleep(4)
print()
print ('The battle begins...')
time.sleep(4)
print()
round = 1

while health1>0 and health2>0:
  damageChar1 = roll(6)
  damageChar2 = roll(6)
  
  if damageChar1 > damageChar2:
    health2 -= damage
    if health2 <=0:
      health2 = 0
    print()
    print()
    print(f'{name1} wins the {round} blow')
    time.sleep(1)
    print(f'{name2} takes a hit, with {damage} damage')
    time.sleep(2)
    print()
    print(f'''{name1} the {type1}
    HEALTH: {health1}''')
    time.sleep(1)
    print()
    print(f'''{name2} the {type2}
    HEALTH: {health2}''')
    time.sleep(2)


    round += 1

  elif damageChar2 > damageChar1:
    health1 -= damage
    if health1 <=0:
      health1 = 0
    print()
    print()
    print(f'{name2} wins the {round} blow')
    time.sleep(1)
    print(f'{name1} takes a hit, with {damage} damage')
    time.sleep(2)
    print()
    print(f'''{name1} the {type1}
    HEALTH: {health1}''')
    time.sleep(1)
    print()
    print(f'''{name2} the {type2}
    HEALTH: {health2}''')
    time.sleep(2)


    round += 1    
  elif damageChar2 == damageChar1:
    time.sleep(2)
    print()
    print()
    print('Draaaaw!!!!')
    time.sleep(1)
    print('Let\'s do it again...')
    time.sleep(3)
    round += 1

if health1 == 0:
  print()
  print()
  time.sleep(3)
  print (f'After {round-1} rounds of exhaisting battle {name2} wins!!!')
else:
  print()
  print()
  time.sleep(3)
  print (f'After {round-1} rounds of exhausting battle {name1} wins!!!')