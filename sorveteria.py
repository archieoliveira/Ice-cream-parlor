#this code is able to sum the value of the customers' order and show on the screen
#the customer has to be able to buy how much ice creams they wants to
#ps: this code is written originally in brazilian portuguese, i translated the variable names and comments but didnt convert the currency

flavor = balls = count = str
value = accumulator = 0
print(' ' * 15, 'WELCOME TO ARTUR ICE-CREAM PARLOR')
print('-' * 37, 'MENU', '-' * 36)
print('| BALL AMOUNT | TRADITIONAL FLAVOR (tr)| PREMIUM FLAVOR (pr)| SPECIAL FLAVOR  (es)|')
print('|      1      |        R$6.00          |       R$7.00       |       R$8.00        |')
print('|      2      |        R$11.00         |       R$13.00      |       R$15.00       |')
print('|      3      |        R$15.00         |       R$18.00      |       R$21.00       |')
print('-' * 83)

while True:
  flavor = input('Enter the flavor: (tr/pr/es) ')
  flavor = flavor.lower() #converting all the possible inputs to lower case, by this, the code is able to get the conditional flowing correctly
  if flavor != 'tr' and flavor != 'pr' and flavor != 'es': #conditional made to test if the user is inserting a valid option
    print('Invalid flavor, try again!')
    continue #returns to the start of the loop while
  while True: #i made this other loop just to 
    balls = input('Enter the amount of balls: (1/2/3) ')
    if balls != '1' and balls != '2' and balls != '3':
      print('Invalid ball amount, try again!')
      continue #this continue returns to the second while loop inside the first one, after validating the flavor
    else:
      break #if the user enters a valid option, returns to the first while loop that continues below
  if balls == '1': #if the user enters the option 1 ball, there is all the possible results below the if
    if flavor == 'tr':
      value = 6.00
    elif flavor == 'pr':
      value = 7.00
    else:
      value = 8.00
  elif balls == '2': #the same thing but with 2 balls
    if flavor == 'tr':
      value = 11.00
    elif flavor == 'pr':
      value = 13.00
    else:
      value = 15.00
  else: #as the only valid options passed the conditionals are 1, 2 or 3 balls, the else can only cover the last option
    if flavor == 'tr':
      value = 15.00
    elif flavor == 'pr':
      value = 18.00
    else:
      value = 21.00
  accumulator += value #this line makes the accumulator variable always add the ice cream value to its own every time the loop happens and store it
  print(f'You chose {balls} balls of the {flavor} flavor') #on each choose, returns to the user what has been ordered
  cont = input('Deseja continuar comprando? (YES/NO) ') #thats what gives the user the possibility to continue buying
  print() #just to do an space
  cont = cont.upper() #converting the input to uppercase just to make it possible to validate through the conditionals
  if cont == 'YES':
    continue #if the user enters "yes", the program continues to the first loop 
  else:
    break #if the user enters "no", the program stops and shows the order's total value 
print(f'The amount to be paid is R${accumulator:.2f} ')