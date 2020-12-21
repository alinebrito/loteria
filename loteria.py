import random
import sys
  
def media(list):
  return sum(list)/len(list)

def lotofacil():
  
  print("\n>Lotofacil: ")

  candidates_1 = list(range(1, 26))
  result_1 = list(sorted(random.sample(candidates_1, 15)))

  candidates_2 = list(set(candidates_1) - set(result_1))
  result_2 = sorted(list(random.sample(result_1, 5)) + candidates_2)

  print('\nJogo 1: {}'.format(result_1))
  print('\nJogo 2: {}'.format(result_2))

  pass

def megasena():
  print("\n>Mega-Sena: ")
  print(sorted(random.sample(range(1, 61), 6)))
  pass

def lotomania():
  print("\n>Lotomania: ")
  result = sorted(list(random.sample(range(0, 100), 50)))
  print(result)

def quina():
  print("\n>Quina: ")
  result = sorted(list(random.sample(range(1, 81), 5)))
  print(result)

def menu(option):
  options = {
    0: sys.exit,
    1: megasena,
    2: lotofacil,
    3: lotomania,
    4: quina
  }
  options[option]()
  pass

def run():
  option = 10
  print('\n\n0 - Exit')
  print('1 - Mega-Sena')
  print('2 - Lotofacil')
  print('3 - Lotomania')
  print('4 - Quina')
  while option != 0:
    option = int(input('\n\nOption: '))
    menu(option)
  pass

run()