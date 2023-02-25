# # Snake Water Gun GAME

# from random import randint
# playerPoint = 0
# attempts = 0
# computerPoints = 0
# totalAttempts = 5
# while True:
    
#     # Computer Turn
#     computerVal = ['Snake', 'Water', 'Gun']
#     computerRand = randint(0, len(computerVal) - 1)
#     computerChoose = computerVal[computerRand]

#     # Player Turn

#     playerChoose = input('''Choose s for snake, g for gun and w for water: \n''')

#     if(playerChoose == 's' and computerChoose == 'Snake'):
#         print('Draw')
#     elif(playerChoose == 'g' and computerChoose=='Snake'):
#         playerPoint+=1
#         attempts+=1
#         totalAttempts-=1
#     elif(playerChoose == 'w' and computerChoose=='Snake'):
#         computerPoints+=1
#         attempts+=1
#         totalAttempts-=1



#     elif(playerChoose == 'w' and computerChoose == 'Water'):
#         print('Draw')
#     elif(playerChoose == 'g' and computerChoose == 'Water'):
#         computerPoints+=1
#         attempts+=1
#         totalAttempts-=1

#     elif(playerChoose == 's' and computerChoose == 'Water'):
#         playerPoint+=1
#         attempts+=1
#         totalAttempts-=1
        
        
        
#     elif(playerChoose == 's' and computerChoose == 'Gun'):
#         computerPoints+=1
#         attempts+=1
#         totalAttempts-=1
        
#     elif(playerChoose == 'g' and computerChoose == 'Gun'):
#         print('Draw')
#     elif(playerChoose == 'w' and computerChoose == 'Gun'):
#         playerPoint+=1
#         attempts+=1
#         totalAttempts-=1
        
        
    
#     print(f"Computer choose {computerChoose}")
#     if (playerChoose == 'w'):
#         print('You choose Water')
#     if (playerChoose == 's'):
#         print('You choose Snake')
#     if (playerChoose == 'g'):
#         print('You choose Gun')

#     print(f"Your Points = {playerPoint}")
#     print(f"Computer Points = {computerPoints}")
    
#     print(f"You have {totalAttempts} attempts left")
#     if (attempts == 5):
#         break

# if computerPoints > playerPoint:
#     print('Game Over You LOSE')
# else:
#     print('Congratulations YOU WON!!')

a = input('Enter you name: \n')

try:
    a
except:
    print('Please give a correct input')