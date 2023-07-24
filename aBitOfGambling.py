import random, time, os

people = {"A": {"odor": 98, "intelligence":12, "money":45, "hair":100},
          "B":{"odor": 100, "intelligence":2, "money":5, "hair":41},
          "C":{"odor": 1000, "intelligence":66, "money":10, "hair":13},
          "D": {"odor": 34, "intelligence":3, "money":99, "hair":2}}

peopleAvailable = people.copy()

print ("TOP TRUMPS")
print ()
print ("Characters:")
print ()
for key in people.keys():
  print (key)
print ()

while True:
  yourCharacter = input("Pick your character > ").strip().title()
  if yourCharacter in people:
    break
  print ("Invalid character. Please try again.")

print ()
time.sleep(0.5)
del peopleAvailable[yourCharacter]

computerPick = random.choice(list(peopleAvailable.keys()))
print (f'The computer has chosen {computerPick}.')
print()
time.sleep(0.7)

while True:
  variable = input ("Choose your stat (odor / intelligence / money / hair) > ").strip().lower()
  if variable in people[yourCharacter]:
    break
  print ("Invalid stat. Please try again.")

x = people[yourCharacter][variable]
y = peopleAvailable[computerPick][variable]

print (f'{yourCharacter}: {x}')
print (f'{computerPick}: {y}')

if peopleAvailable[computerPick][variable] > people[yourCharacter][variable]:
  print (f'{computerPick} wins!')
else:
  print (f'{yourCharacter} wins!')
