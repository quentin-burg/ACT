import sys
from v_dynamique import *

# pour utiliser les arguments en ligne de commande
"""for arf in sys.argv :
    print arg
"""

"""
    TODO :
    - faire en sorte de pouvoir lancer en ligne de commande
"""


def game(m,n,i,j):
    display(m,n,i,j)
    current_player=2
    while (m != 1 or n !=1):
        print()
        print('TOUR DU JOUEUR : ', current_player)
        print('LA CONFIGURATION ACTUELLE EST : ', (m,n,i,j))
        #tour de l'ordinateur
        if(current_player == 2):
            # calcul du score
            score = v_dynamique(m,n,i,j)
            print('Le score de l\'ordinateur est : ' , score)
            # calcul de la configuration choisie par l'ordinateur
            if (score < 0):
                val = -(score+1)
            else :
                val = -(score-1)
            if (val == 0):
                (m,n,i,j) = (1,1,0,0)
            else :
                (m,n,i,j) = getvalue(val)[0]
            current_player=1
        else:
            sideInput = manageSideInput(m,n)
            valueInput = manageValueInput(m,n)
            (m,n,i,j) = computeConfig((m,n,i,j), sideInput=="h", valueInput)
            calcul = v_dynamique(m,n,i,j)
            current_player=2
        print('LA NOUVELLE CONFIGURATION EST :  ', (m,n,i,j))
        display(m,n,i,j)
    print('LE JOUEUR ',current_player,' A PERDU')


def computeConfig( config, direction, position):
    if (direction):  ## direction = False => horizontal
        if (position > config[3]):
            return (config[0], config[1]-(config[1]-position), config[2], config[3])
        else:
            return (config[0], config[1]-position, config[2], config[3]-position)
    else:
        if (position > config[2]):
            return (config[0] - (config[0]-position), config[1], config[2] , config[3])
        else:
            return (config[0]-position, config[1] , config[2] -position, config[3])


def display(m,n,i,j):
    
    for a in range(0,n):
        for b in range (0,m):
            if(a == j and b == i):
                print(u'\u25A0 ',end="")
            else:
                print(u'\u25A1 ',end="")
        print("")

def manageSideInput(m,n):
    side =input("""De quel côté souhaitez - vous couper ? (h = horizontalement / v = verticalement)  :  """)
    if (side != 'h' and side!= 'v'):
        return manageSideInput(m,n)
    if (m == 1 and side == 'v'):
        print('Vous ne pouvez plus couper verticalement !')
        return manageSideInput(m,n)
    if (n == 1 and side == 'h'):
        print('Vous ne pouvez plus couper horizontalement !')
        return manageSideInput(m,n)
    return side

    

def manageValueInput(m,n):
    v = input("""Combien de carrés coupez-vous ?  :  """)
    for i in v :
        if (ord(i) < ord('0') or ord(i) > ord ('9')):
            return manageValueInput(m,n)
    if (v ==''):
        return manageValueInput(m,n)
    v = int(v)
    return v if (v > 0 and (v < m or v < n)) else manageValueInput(m,n)

    
game(4,4,2,2)
