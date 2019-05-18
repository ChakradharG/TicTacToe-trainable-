# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:14:38 2019

@author: Chakradhar
"""

import random as r
import T3_Core as z

winner_dict = {-1:'Its a Tie', 0:'Winner: CPU! Better Luck Next Time', 1:'Winner: Human!'}
board_dict = {-1:'_', 0:'O', 1:'X'}
board = [[-1 for i in range(3)] for j in range(3)]
winner = -1
w = {-1:1, 0:1, 1:0}
moves_made = []
b = ()
q = 0

def print_b():
    for i in range(3):
        for j in range(3):
            print(board_dict[board[i][j]], end=' ')
        print('\n')

def is_avail(i, j):
    return board[i][j] == -1

def update():
    while True:
        try:
            x = int(input('Your Move: '))
            if x not in [1,2,3,4,5,6,7,8,9]:
                raise ValueError
            i = int((x-1)//3)
            j = int((x-1)%3)
            if is_avail(i, j):
                break
            else:
                print('Illegal Move! Try Again')
                continue
        except:
            print('Wrong Input. Try again')
            continue
    board[i][j] = 1

def move_provider():
    yield z.m2.m
    yield z.m4.m
    yield z.m6.m
    yield z.m8.m
f = move_provider()

def board_conv():
    global b
    l_1, l_2 = [], []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                l_1.append(3*i + j + 1)
            elif board[i][j] == 0:
                l_2.append(3*i + j + 1)
    b = tuple(l_1 + l_2)

def cpu_move():
    board_conv()
    global b
    d = next(f)
    x = r.choice(d[b])
    #print(b, ': ', d[b], sep='')  #Uncomment This to View/Debug the Learning Process
    b = list(b)
    b.append(x)
    moves_made.append(b)
    i, j = (x-1)//3, (x-1)%3
    board[i][j] = 0
    print('CPU\'s Move:', x)

def learn():
    global q
    if q == 9:
        x = moves_made[-1]
        y = x[-1]
        moves_made.remove(moves_made[-1])
        x.remove(y)
        x = tuple(x)
        if z.m8.length(x) > 1:
            z.m8.rem_bad_mov(x, y)
        else:
            q -= 2
    if q == 7:
        x = moves_made[-1]
        y = x[-1]
        moves_made.remove(moves_made[-1])
        x.remove(y)
        x = tuple(x)
        if z.m6.length(x) > 1:
            z.m6.rem_bad_mov(x, y)
        else:
            q -= 2
    if q == 5:
        x = moves_made[-1]
        y = x[-1]
        moves_made.remove(moves_made[-1])
        x.remove(y)
        x = tuple(x)
        if z.m4.length(x) > 1:
            z.m4.rem_bad_mov(x, y)
        else:
            q -= 2
    if q == 3:
        x = moves_made[-1]
        y = x[-1]
        moves_made.remove(moves_made[-1])
        x.remove(y)
        x = tuple(x)
        if z.m2.length(x) > 1:
            z.m2.rem_bad_mov(x, y)

def decider(t):
    global winner
    #Win by rows
    for i in board:
        cur = 0
        for j in i:
            if j == t:
                cur += 1
        if cur == 3:
            winner = t
            return True
    #Win by columns
    for i in range(3):
        cur = 0
        for j in range(3):
            if board[j][i] == t:
                cur += 1
        if cur == 3:
            winner = t
            return True
    #Win by diagonal0
    for i in range(3):
        if board[i][i] != t:
            break
    else:
        winner = t
        return True
    #Win by diagonal1
    cur = 0
    for i in range(3):
        if board[i][2-i] != t:
            break
    else:
        winner = t
        return True
    #No Winner yet
    return False

print('Hello & Welcome to TicTacToe')
ch = 'y'
while ch == 'y':
    board = [[-1 for i in range(3)] for j in range(3)]
    winner = -1
    moves_made = []
    b = ()
    q = 0
    print('Current Board is:')
    print_b()
    print('Enter your move as a number between 1 to 9')
    for count in range(5):
        update()
        q += 1
        print_b()
        if decider(1) or count == 4:
            break
        print('\n')
        cpu_move()
        q += 1
        print_b()
        if decider(0):
            break
    print(winner_dict[winner])
    z.win_list.append(w[winner])
    if winner == 1:
        learn()
    f = move_provider()
    while True:
        ch = input('Want to Play Again? (y/n)')
        if ch in ('y', 'n'):
            break
        else:
            print('Wrong Input')
print('Thank You for playing!')

z.writeback()
c = input('Would You Like to See the Stats? (y)')
if c == 'y':
    z.stats()
