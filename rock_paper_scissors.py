import random
import rps_imports

print('This is ROCK-PAPAER-SCISSOR GAME')
player_name = input('please enter your name')
print('enter your choice 0:rock 1:paper 2:scissor')
player_choice = int(input('choose a number b/w 0-2'))

if rps_imports.validate(player_choice):
    rps_imports.player_game(player_name,player_choice)
    
    options = ['rock','paper','scissor']
    pc_choice = random.randint(0,2)
    print('pc selected '+options[pc_choice])

    result = rps_imports.evaluation(player_choice,pc_choice)
    print(result)
else:
    print('entered number out of bound')    


