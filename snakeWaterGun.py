# SNAKE WATER OR GUN
# Computer choose snake and you choose gun so you will win
# Computer choose water and you choose snake so you will win
# Computer choose gun and you choose water so you will win

from random import randint
playerName = input('Enter you name: \n')
print(f"Welcome {playerName} let's play SNAKE WATER GUN GAME")
print('You have only 5 attempts, and whoever has the highest point will win')
playerPoints = 0
computerPoint = 0
attempts = 0
totalAttempts = 5
while True:
    # Computer Turn
    computerVal = ['Snake', 'Water', 'Gun']
    computerRand = randint(0, len(computerVal) - 1)
    computerChoose = computerVal[computerRand]


    # Player Turn
    playerChoose = input('Choose g for Gun, w for Water and s for Snake: \n')
    if (playerChoose != 'g' or playerChoose != 'w' or playerChoose != 's'):
        print(f'Please {playerName} choose a valid input')
    # condition to check who wins
    
    # If computer choose snake
    if (playerChoose == 'g' and computerChoose == 'Snake'):
        computerPoint+=1
        attempts+=1
        totalAttempts-=1
    elif (playerChoose == 's' and computerChoose == 'Snake'):
        print('Draw')
    elif (playerChoose == 'w' and computerChoose == 'Snake'):
        playerPoints+=1
        attempts+=1
        totalAttempts-=1



    # If computer choose gun
    elif (playerChoose == 'g' and computerChoose == 'Gun'):
        print('Draw')
    elif (playerChoose == 's' and computerChoose == 'Gun'):
        computerPoint+=1
        attempts+=1
        totalAttempts-=1


    elif (playerChoose == 'w' and computerChoose == 'Gun'):
        playerPoints+=1
        attempts+=1
        totalAttempts-=1



    # If computer choose Water
    elif (playerChoose == 'g' and computerChoose == 'Water'):
        computerPoint+=1
        attempts+=1
        totalAttempts-=1


    elif (playerChoose == 's' and computerChoose == 'Water'):
        playerPoints+=1
        attempts+=1
        totalAttempts-=1


    elif (playerChoose == 'w' and computerChoose == 'Water'):
        print('Draw')

    print(f'Computer choose {computerChoose}')
    if(playerChoose == 'g'):
        print(f'{playerName} choose Gun')
    if(playerChoose == 's'):
        print(f'{playerName} choose Snake')
    if(playerChoose == 'w'):
        print(f'{playerName} choose Water')


    print(f"{playerName}'s Points = {playerPoints}")
    print(f"Computer Points = {computerPoint}")

    print(f"You have {totalAttempts} attempts left")

    if(attempts == 5):
        break


if computerPoint > playerPoints:
    print(f'GAME OVER {playerName}, YOU LOSE')
else:
    print(f'CONGRATULATIONS {playerName}, YOU WON!!')


