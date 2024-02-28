from random import shuffle


class Card:
  suits = ['pik', 'kier', 'karo', 'trefl']
  values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'waleta', 'damę', 'króla', 'asa']

  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def __lt__(self, other):
    if self.value < other.value:
      return True
    if self.value == other.value:
      if self.suit < other.suit:
        return True
      else:
        return False
    return False

  def __gt__(self, other):
    if self.value > other.value:
      return True
    if self.value == other.value:
      if self.suit > other.suit:
        return True
      else:
        return False
    return False

  def __repr__(self):
    return self.values[self.value] + ' ' + self.suits[self.suit]


class Deck:
  def __init__(self):
    self.cards = []
    for i in range (2,15):
      for j in range (4):
        self.cards.append(Card(i, j))
    shuffle(self.cards)

  def rm_card(self):
    if len(self.cards) == 0:
      return
    return self.cards.pop()


class Player:
  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name


class Game:
  
