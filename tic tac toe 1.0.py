import random
import time
from time import sleep
print('This is a project, for a tic tac toe game, further versions will be released in the future')
sleep(1)
tic= str(input('Enter the choice, type "R" for rock, "P" for paper, "S" for scissor: '))
sleep(1.5)
x= ['Rock', 'Paper', 'Scissor']
result=(f"I choose {random.choice(x)}")
print(result)
sleep(0.5)
if result == tic:
    print('TIE')
elif tic == 'R' and result == 'I choose Paper':
    print('You lose!')
elif tic == 'R' and result == 'I choose Scissor':
    print('You Win!')
elif tic == 'P' and result == 'I choose Rock':
    print('You Win!')
elif tic == 'P' and result == 'I choose Scissor':
    print('You lose!')
elif tic == 'S' and result == 'I choose Rock':
    print('You lose!')
elif tic == 'S' and result == 'I choose Paper':
    print('You Win!')






