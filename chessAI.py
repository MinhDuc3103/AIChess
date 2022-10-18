import sys
import random
from turtle import left

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    pass

#############################################################################
######## Board
#############################################################################
class Board:
    pass

#############################################################################
######## State
#############################################################################
class State:
    pass
def toString(row, col):
    return (chr(col + 97), row)

def checkKing(row, col, n, m, gameboard, value):
    ls = []
    for i in  range (-1, 2):
        for j in range(-1, 2): 
            if i == 0 and j == 0: continue
            if check(row + i, col + j, n, m):
                if (row + i, col + j) not in gameboard or ((row + i, col + j) in gameboard and gameboard[(row + i, col + j)][1] != value):
                    ls.append((row + i,col + j))
    return ls 

def check(row, col, n, m):
    return (0 <= row < n) and (0 <= col < m)

def checkRook(row, col, n, m, gameboard, value):
    ls = []
    i = 1
    while(check(row - i, col, n, m)): 
        if (row - i, col) not in gameboard:
            ls.append((row - i, col))
        elif gameboard[(row - i, col)][1] != value:
            ls.append((row - i , col))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row + i, col, n, m)): 
        if (row + i, col) not in gameboard:
            ls.append((row + i, col))
        elif gameboard[(row + i, col)][1] != value:
            ls.append((row + i, col))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row, col - i, n, m)): 
        if (row, col - i) not in gameboard:
            ls.append((row, col - i))
        elif gameboard[(row, col - i)][1] != value:
            ls.append((row, col - i))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row, col + i, n, m)): 
        if (row, col + i) not in gameboard:
            ls.append((row, col + i))
        elif gameboard[(row, col + i)][1] != value:
            ls.append((row, col + i))
            break
        else:
            break
        i += 1
    return ls

def checkBishop(row, col, n, m, gameboard, value):
    ls = []
    i = 1
    while(check(row - i, col - i, n, m)): 
        if (row - i, col - i) not in gameboard:
            ls.append((row - i, col - i))
        elif gameboard[(row - i, col - i)][1] != value:
            ls.append((row - i, col - i))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row + i, col + i, n, m)): 
        if (row + i, col + i) not in gameboard:
            ls.append((row + i, col + i))
        elif gameboard[(row + i, col + i)][1] != value:
            ls.append((row + i, col + i))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row + i, col - i, n, m)): 
        if (row + i, col - i) not in gameboard:
            ls.append((row + i, col - i))
        elif gameboard[(row + i, col - i)][1] != value:
            ls.append((row + i, col - i))
            break
        else:
            break
        i += 1
    i = 1
    while(check(row - i, col + i, n, m)): 
        if (row - i, col + i) not in gameboard:
            ls.append((row - i, col + i))
        elif gameboard[(row - i, col + i)][1] != value:
            ls.append((row - i, col + i))
            break
        else:
            break
        i += 1
    return ls

def checkQueen(row, col, n, m, gameboard, value):
    a = checkRook(row, col, n, m, gameboard, value)
    c = checkBishop(row, col, n, m, gameboard, value)
    return a + c

def checkKnight(row, col, n, m, gameboard, value):
    ls = []
    if (check(row - 1, col - 2, n, m)):
        if (row - 1, col - 2) not in gameboard or ((row - 1, col - 2) in gameboard and gameboard[(row - 1, col - 2)][1] != value):
            ls.append((row - 1, col - 2))
    if (check(row - 2, col - 1, n, m)):
        if (row - 2, col - 1) not in gameboard or ((row - 2, col - 1) in gameboard and gameboard[(row - 2, col - 1)][1] != value):
            ls.append((row - 2, col - 1))


    if (check(row + 1, col + 2, n, m)):
        if (row + 1, col + 2) not in gameboard or ((row + 1, col + 2) in gameboard and gameboard[(row + 1, col + 2)][1] != value):
            ls.append((row + 1, col + 2))
    if (check(row + 2, col + 1, n, m)):
        if (row + 2, col + 1) not in gameboard or ((row + 2, col + 1) in gameboard and gameboard[(row + 2, col + 1)][1] != value):
            ls.append((row + 2, col + 1))


    if (check(row - 2, col + 1, n, m)):
        if (row - 2, col + 1) not in gameboard or ((row - 2, col + 1) in gameboard and gameboard[(row - 2, col + 1)][1] != value):
            ls.append((row - 2, col + 1))
    if (check(row - 1, col + 2, n, m)):
        if (row - 1, col + 2) not in gameboard or ((row - 1, col + 2) in gameboard and gameboard[(row - 1, col + 2)][1] != value):
            ls.append((row - 1, col + 2))


    if (check(row + 1, col - 2, n, m)):
        if (row + 1, col - 2) not in gameboard or ((row + 1, col - 2) in gameboard and gameboard[(row + 1, col - 2)][1] != value):
            ls.append((row + 1, col - 2))
    if (check(row + 2, col - 1, n, m)):
        if (row + 2, col - 1) not in gameboard or ((row + 2, col - 1) in gameboard and gameboard[(row + 2, col - 1)][1] != value):
            ls.append((row + 2, col - 1))

    return ls

def checkFerz(row, col, n, m, gameboard, value):
    ls = []
    if (check(row - 1, col - 1, n, m)):
        if (row - 1, col - 1) not in gameboard or ((row - 1, col - 1) in gameboard and gameboard[(row - 1, col - 1)][1] != value):
            ls.append((row - 1, col - 1))

    if (check(row - 1, col + 1, n, m)):
        if (row - 1, col + 1) not in gameboard or ((row - 1, col + 1) in gameboard and gameboard[(row - 1, col + 1)][1] != value):
            ls.append((row - 1, col + 1))

    if (check(row + 1, col + 1, n, m)):
        if (row + 1, col + 1) not in gameboard or ((row + 1, col + 1) in gameboard and gameboard[(row + 1, col + 1)][1] != value):
            ls.append((row + 1, col + 1))

    if (check(row + 1, col - 1, n, m)):
        if (row + 1, col - 1) not in gameboard or ((row + 1, col - 1) in gameboard and gameboard[(row + 1, col - 1)][1] != value):
            ls.append((row + 1, col - 1))

    return ls

def checkPrincess(row, col, n, m, gameboard, value):
    a = checkBishop(row, col, n, m, gameboard, value)
    c = checkKnight(row, col, n, m, gameboard, value)
    return a + c

def checkEmpress(row, col, n, m, gameboard, value):
    a = checkKnight(row, col, n, m, gameboard, value)
    c = checkRook(row, col, n, m, gameboard, value)
    return a + c

def checkPawnBlack(row ,col, n, m, gameboard, value):
    ls = []
    if (check(row + 1, col, n, m)) and (row + 1, col) not in gameboard:
        ls.append((row + 1, col))
    if (check(row + 1, col - 1, n, m)) and (row + 1, col - 1) in gameboard and gameboard[(row + 1, col - 1)][1] != value:
        ls.append((row + 1, col - 1))
    if (check(row + 1, col + 1, n, m)) and (row + 1, col + 1) in gameboard and gameboard[(row + 1, col + 1)][1] != value:
        ls.append((row + 1, col + 1))
    if (row == 1):
        if (check(row + 2, col, n, m)) and (row + 2, col) not in gameboard and (row + 1, col) not in gameboard:
            ls.append((row + 2, col))
    return ls

def checkPawnWhite(row ,col, n, m, gameboard, value):
    ls = []
    if (check(row - 1, col, n, m)) and (row - 1, col) not in gameboard:
        ls.append((row - 1, col))
    if (check(row - 1, col - 1, n, m)) and (row - 1, col - 1) in gameboard and gameboard[(row - 1, col - 1)][1] != value:
        ls.append((row - 1, col - 1))
    if (check(row - 1, col + 1, n, m)) and (row - 1, col + 1) in gameboard and gameboard[(row - 1, col + 1)][1] != value:
        ls.append((row - 1, col + 1))
    if (row == 6):
        if (check(row - 2, col, n, m)) and (row - 2, col) not in gameboard and (row - 1, col) not in gameboard:
            ls.append((row - 2, col))
    return ls

#Implement your minimax with alpha-beta pruning algorithm here.
def cost(gameboard, potential_value):
    piece_cost_early = {'Pawn' : 198,'Knight' : 817, 'Rook' : 1270, 'Bishop' : 836, 'Queen' : 2521,  'King': 1000000}
    piece_cost_late =  {'Pawn' : 300,'Knight' : 846, 'Rook' : 1281, 'Bishop' : 857, 'Queen' : 2558,  'King': 1000000}
    
    if ('King', 'Black') not in gameboard.values():
        return -1000000

    ans = 0
    if len(gameboard) <= 18:
        for i in gameboard:
            if gameboard[i][1] == 'Black':
                ans += piece_cost_late[gameboard[i][0]]
                if gameboard[i][0] == 'Pawn':
                    if i[1] <= 5:
                        ans += 50*(6 - i[1])
                    else:
                        ans += 400
            else:
                ans -= piece_cost_late[gameboard[i][0]]
                if gameboard[i][0] == 'Pawn':
                    if i[1] <= 5:
                        ans -= 50*(6 - i[1])
                    else:
                        ans -= 400
    else:
        for i in gameboard:
            if gameboard[i][1] == 'Black':
                ans += potential_value[i[0]][i[1]]
                ans += piece_cost_early[gameboard[i][0]]
            else:
                ans -= piece_cost_early[gameboard[i][0]]
                ans -= potential_value[i[0]][i[1]]
            
    return ans

def findMove(piece, row, col, rows, cols, gameboad, value):
    moves = []
    if piece == 'Pawn':
        if value == 'White':
            moves = checkPawnWhite(row, col, rows, cols, gameboad, value)
        else:
            moves = checkPawnBlack(row, col, rows, cols, gameboad, value)
    elif piece == 'Ferz':
        moves = checkFerz(row, col, rows, cols, gameboad, value)
    elif piece == 'Knight':
        moves = checkKnight(row, col, rows, cols, gameboad, value)
    elif piece == 'Bishop':
        moves = checkBishop(row, col, rows, cols, gameboad, value)
    elif piece == 'Rook':
        moves = checkRook(row, col, rows, cols, gameboad, value)
    elif piece == 'Empress':
        moves = checkEmpress(row, col, rows, cols, gameboad, value)
    elif piece == 'Princess':
        moves = checkPrincess(row, col, rows, cols, gameboad, value)
    elif piece == 'Queen':
        moves = checkQueen(row, col, rows, cols, gameboad, value)
    elif piece == 'King':
        moves = checkKing(row, col, rows, cols, gameboad, value)
    return moves
    
def ab(gameboard):
    rows = 8
    cols = 8

    potential_value = []
    for i in range (rows):
        tem = []
        for j in range(cols):
            tem.append(0)
        potential_value.append(tem)
    for i in range (8):
        for j in range(8):
            if 3 <= i <= 4 and 3 <= j <= 4:
                potential_value[i][j] = 40
            elif 3 <= i <= 4 :
                potential_value[i][j] = 20

    MAX, MIN = 1000000, -1000000
    best_move = {0 : "No move"}
    def minimax(depth, gameboard, isMaxPlayer, alpha, beta):
  
        if depth == 5:
            return cost(gameboard, potential_value)
    
        if isMaxPlayer:
        
            best = MIN
            next = []
            for i in gameboard:
                if gameboard[i][1] == 'Black':
                    moves = findMove(gameboard[i][0], i[0], i[1], rows, cols, gameboard, gameboard[i][1])
                    for move in moves:
                        next.append((i, move))
            random.shuffle(next)
            for children in next:
                tem_gameboard = gameboard.copy()
                if tem_gameboard[children[0]][0] == 'Pawn' and children[1][0] == 7:
                    tem_gameboard[children[1]] = ('Queen', 'Black')
                else:
                    tem_gameboard[children[1]] = tem_gameboard[children[0]]
                tem_gameboard.pop(children[0])
                val = minimax(depth + 1, tem_gameboard, False, alpha, beta)
                if best < val:
                    best_move[depth] = children
                    best = val


                alpha = max(alpha, best)

                if beta <= alpha:
                    break
                        
            return best
        
        else:
            best = MAX
    
            next = []
            for i in gameboard:
                if gameboard[i][1] == 'White':
                    moves = findMove(gameboard[i][0], i[0], i[1], rows, cols, gameboard, gameboard[i][1])
                    for move in moves:
                        next.append((i, move))

            random.shuffle(next)
            for children in next:
                tem_gameboard = gameboard.copy()
                if tem_gameboard[children[0]][0] == 'Pawn' and children[1][0] == 7:
                    tem_gameboard[children[1]] = ('Queen', 'White')
                else:
                    tem_gameboard[children[1]] = tem_gameboard[children[0]]
                tem_gameboard.pop(children[0])
                val = minimax(depth + 1, tem_gameboard, True, alpha, beta)
                if best > val:
                    best_move[depth] = children
                    best = val
                beta = min(beta, best)
            
                if beta <= alpha:
                    break

            return best
    minimax(0, gameboard, True, MIN, MAX)
    
    if best_move[0] == "No move":
        return ()
    return best_move[0][0], best_move[0][1]
     

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions

# You may call this function if you need to set up the board
def setUpBoard():
    gameboard = {(7, 4): ('King', 'White'), (7, 3): ('Queen', 'White'), 
    (7, 2): ('Bishop', 'White'), (7, 5): ('Bishop', 'White'), (7, 1): ('Knight', 'White'), (7, 6): ('Knight', 'White'), (7, 0): ('Rook', 'White'), (7, 7): ('Rook', 'White'), 
    (6, 0): ('Pawn', 'White'), (6, 1): ('Pawn', 'White'), (6, 2): ('Pawn', 'White'), (6, 3): ('Pawn', 'White'), (6, 4): ('Pawn', 'White'), (6, 5): ('Pawn', 'White'), 
    (6, 6): ('Pawn', 'White'), (6, 7): ('Pawn', 'White'), (0, 4): ('King', 'Black'), (0, 3): ('Queen', 'Black'), (0, 2): ('Bishop', 'Black'), (0, 5): ('Bishop', 'Black'), 
    (0, 1): ('Knight', 'Black'), (0, 6): ('Knight', 'Black'), (0, 0): ('Rook', 'Black'), (0, 7): ('Rook', 'Black'), (1, 0): ('Pawn', 'Black'), (1, 1): ('Pawn', 'Black'), 
    (1, 2): ('Pawn', 'Black'), (1, 3): ('Pawn', 'Black'), (1, 4): ('Pawn', 'Black'), (1, 5): ('Pawn', 'Black'), (1, 6): ('Pawn', 'Black'), (1, 7): ('Pawn', 'Black')}
    return gameboard
    
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(gameboard)
    return move #Format to be returned (('a', 0), ('b', 3))
