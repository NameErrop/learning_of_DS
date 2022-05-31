"""A number guessing game"""
import numpy as np
number = np.random.randint(1,101) # We make a number
count = 0
while True:
    count+=1
    predict_number = int(input('Guess the numdber from 1 to 100:  '))
    
    if predict_number > number:
        print('The numder must be less than')
        
    elif predict_number < number:
        print('The number must de greater than')
        
    else:
        print(f'You guessed the number! This number is {number} in {count} attempts')
        break # End of the game, exit the loop.
