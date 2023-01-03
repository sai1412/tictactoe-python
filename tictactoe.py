import os
def TheEnd():
    p=0
    for x in range(0,8):
        for y in range(0,3):
            if y==0:
                p=board[test[x][y]]
                if p==0:
                    break
            elif board[test[x][y]] != p:
                    break
            if y==2:
                os.system("cls")
                display()
                print(f"{decode(p)} is the WINNER!!!")
                return True
    return False

def IsLegal(x):
    if x>8 or x<0:
        return False
    elif board[x]==0:
        return True
    return False
def decode(id):
    if id==2:
        return 'X'
    elif id==1:
        return 'O'
    return ' '

def display():
    print("-------------")
    print(f"| {decode(board[0])} | {decode(board[1])} | {decode(board[2])} |")
    print("-------------")
    print(f"| {decode(board[3])} | {decode(board[4])} | {decode(board[5])} |")
    print("-------------")
    print(f"| {decode(board[6])} | {decode(board[7])} | {decode(board[8])} |")
    print("-------------")
board = [0,0,0,
        0,0,0,
        0,0,0]
test=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,7],
    [2,4,6]]
isX_Turn=True
count=0
while(not(TheEnd())):
    os.system("cls")  
    display()
    if isX_Turn==True:
        print("X's TURN ")
    else:
        print("Y's TURN ")
    x=int(input("Enter a position : "))-1
    if IsLegal(x) == True:
        count+=1
        if isX_Turn == True:
            board[x]=2
            isX_Turn= False
        else:
            board[x]=1
            isX_Turn=True
    else:
        print("select a valid position")
    if count==9:
        os.system("cls")
        display()
        print("DRAW!!!")
        break



