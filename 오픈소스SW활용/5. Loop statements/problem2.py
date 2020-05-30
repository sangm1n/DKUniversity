"""
Consider some game where each participant draws a series of random integers evenly distributed from 0 to 10,
with the aim of getting the sum as close as possible to 21, but not larger than 21.
You are out of the game if the sum passes 21.
After each draw, you are told the number and is asked whether you want another draw or not.
The one coming closest to 21 is the winner. Implement this game.
"""

import numpy as np

sum = 0
while True:
    rand = np.random.randint(0, 11)
    sum += rand

    if sum > 21:
        print('\nOops.. computer wins the game, your total number is', sum)
        break

    print('your number is', rand, 'and total is', sum)
    answer = input('if you draw more card ? (yes/no) ')

    if answer == 'yes':
        continue
    else:
        print('\nCongratulation ! your total number is', sum)
        break

