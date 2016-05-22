## Collatz sequence

def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return(number // 2)
  else:
    print(3*number + 1)
    return(3*number + 1)


inputOK = False
while not inputOK:
  try:
    print('Enter an integer to start the Collatz sequence:')
    n = int(input())
    inputOK = True
  except ValueError:
    print('That\'s not an integer! Try again below ...\n')


while n > 1:
  n = collatz(n)



