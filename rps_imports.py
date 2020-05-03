def validate(choice):
    if choice<0 or choice>2:
        return False
    return True

def player_game(name,choice):
    options = ['rock','paper','scissor']
    print(name+' selected '+options[choice])


def evaluation(pl_c,pc_c):
    if pl_c==0 and pc_c==1:
        return 'u lose'
    elif pl_c==1 and pc_c==2:
        return 'u lose'
    elif pl_c==2 and pc_c==0:
        return 'u lose'
    elif pl_c == pc_c:
        return 'Draw'
    else:
        return 'u win'     
