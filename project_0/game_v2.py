"""The game guess the number"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101) # Estimated number
        if number == predict_number:
            break # Exit the loop
    return count

#print(f'Number of attempts: {random_predict()}')
def score_game(random_predict) -> int:
    """The average number out of 1000 approaches

    Args:
        random_predict (_type_): guessing functuin

    Returns:
        int: average number of attempts
    """
    count_ls = [] # list for save numer of attempts
    np.random.seed(1) # Fixing seed for reproducibility
    random_array = np.random.randint(1,101,size=(1000)) # list of numbers
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # find average number of attempts
    print(f' Your algorithm guess number in average of {score} attemtps')
    return score

if __name__ == '__main__':
    #RUN
    score_game(random_predict)