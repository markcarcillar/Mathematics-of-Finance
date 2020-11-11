'''
  Compound Interest - It is an interest computed based on the original principal and the 
                accumulated past interest.

  Formula: A = P(1+r/n)^nt
  Where:
  A - Compound Interest
  P - Principal Amount
  R - Rate
  N - Conversion Period (Eg. Annually, Monthly, Quarterly)
  T - Number of years or time
'''

from time import sleep

on = True
while on:
  try:
    print('Compound Interest. Only enter a number.')
    principal = float(input('Principal amount: '))
    rate = float(input('Rate (Give the decimal value. Example: .10)\n'))
    conversion_period = float(input('Conversion period: '))
    time = float(input('Number of years: '))
    compound_interest = principal * (1 + rate / conversion_period)**(conversion_period*time)
    sleep(2)
    print(f'----> Compound Interest: {compound_interest}')
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