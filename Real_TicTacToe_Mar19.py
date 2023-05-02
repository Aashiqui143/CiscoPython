import random
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for j in range(len(board)):
        print("+-------+-------+--------+")
        print("|       |       |        +")
        print("|  {0}    |  {1}    |   {2}    |".format(board[j][0],board[j][1],board[j][2]))
        print("|       |       |        |")
    print("+-------+-------+--------+")
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    usernum=int(input("Enter a num(1-9) = "))
    if usernum<0 or usernum>9 or type(usernum)!=int:
        print("Wrong input")
        enter_move(board)
    elif usernum in userinplist or usernum in compinplist:
        print("This number is filled, Enter another number")
        enter_move(board)
    else:
        userinplist.append(usernum)
        totalnum.remove(usernum)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==usernum:
                    board[i][j]='o'
    display_board(board)
    victory_for(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!="o" and board[i][j]!="x":
                z=(i,j)
                free_list.append(z)
    print("The number of index position, which are free yet = ",free_list)
                
    

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(len(board)):
        if board[i][0]==board[i][1]==board[i][2]=='x' or board[0][i]==board[1][i]==board[2][i]=='x' or board[0][0]==board[1][1]==board[2][2]=='x':
            print("Game over, Computer Won this game.")
            exit()
        elif  board[i][0]==board[i][1]==board[i][2]=='o' or board[0][i]==board[1][i]==board[2][i]=='o' or board[0][0]==board[1][1]==board[2][2]=='o':
                print("-------------Game over---------------\nCongratulations "+username+", you Won this Game.")
                exit()

    
            
            

userinplist=[]
compinplist=[]
def draw_move(board):
    # The function draws the computer's move and updates the board.
    usernum2=random.choice(totalnum)
    print("Computer number = ",usernum2)
    
    if usernum2 in userinplist or usernum2 in compinplist:
        print("Computer, number is filled, Enter another number")
        draw_move(board)
    else:
        compinplist.append(usernum2)
        totalnum.remove(usernum2)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==usernum2:
                    board[i][j]='x'
        
                    
    display_board(board)
    victory_for(board)
    
board=[]
count=0
totalnum=[]
username=input("Hello user, Please enter your name = ")
if __name__=="__main__":
    for i in range(3):
        row=[]
        for j in range(3):
            count+=1
            row.append(count)
            totalnum.append(count)
        board.append(row)
        del row
        


    display_board(board)
    while True:
        draw_move(board)
        if len(totalnum)==0:
            print("OOPS, The Game was a draw.")
            exit()
        enter_move(board)
        make_list_of_free_fields(board)
