import random
import sys
  
def lotofacil():
  print("\n>Lotofacil: ")
  print(sorted(random.sample(range(1, 26), 15)))
  pass

def megasena():
  print("\n>Mega-Sena: ")
  print(sorted(random.sample(range(1, 61), 6)))
  pass

def lotomania():
  print("\n>Lotomania: ")
  result = sorted(list(random.sample(range(0, 100), 50)))
  print(result)

def menu(option):
  options = {
    0: sys.exit,
    1: megasena,
    2: lotofacil,
    3: lotomania
  }
  options[option]()
  pass

def run():
  option = 10
  print('\n\n0 - Exit')
  print('1 - Mega-Sena')
  print('2 - Lotofacil')
  print('3 - Lotomania')
  while option != 0:
    option = int(input('\n\nOption: '))
    menu(option)
  pass

run()