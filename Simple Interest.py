'''
  Simple Interest - It is an interest computed based on the original principal during the 
              whole life of investment.

  Formula: I = Prt
  Where:
  I - Simple Interest
  P - Principal Amount
  R - Rate (Eg. .10, .05)
  T - Time or Number of years
'''

from time import sleep

on = True
while on:
  try:
    print('Simple Interest. Only enter a number.')
    principal = float(input('Principal Amount: '))
    rate = float(input('Rate (Give the decimal value. Example: .10)\n'))
    time = float(input('Number of years: '))
    simple_interest = principal * rate * time
    sleep(2)
    print(f'----> Simple Interest: {simple_interest}')
    sleep(2)
    _continue = input('Do you want to continue?\na.) Yes\nb.) No\nYour answer: ')
    if _continue.lower() in ['b','no']:
      on = False
    elif _continue.lower() in ['a', 'yes']:
      on = True
    else:
      on = True
      print('You did not enter a valid answer. It will continue.')
  except ValueError:
    print('Please enter a valid number!')
  except KeyboardInterrupt:
    print('Program has been stopped.')
    on = False
  
