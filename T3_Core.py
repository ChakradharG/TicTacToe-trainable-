# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:54:39 2019

@author: Chakradhar
"""

class moves:
    def __init__(self,m):
        self.m = m
    def rem_bad_mov(self,x,y):
        self.m[x].remove(y)
        #print('Removed Bad Move:',x,':',y)  #Uncomment This to View/Debug the Learning Process
        #print(self.m[x])  #Uncomment This to View/Debug the Learning Process
    def length(self,x):
        return len(self.m[x])

win_list = []
       
#Initialization Part
#s = {1,2,3,4,5,6,7,8,9}   #Uncomment This to Reset Training Data
f = open('T3_board.txt','r')
g = open('T3_do.txt','r')

#For Move2
d = {}
for i in range(9):
    a = f.readline().rstrip()
    a = tuple(map(int,a.split(',')))
    #b = set(a)   #Uncomment This to Reset Training Data
    #e = list(s - {a})   #Uncomment This to Reset Training Data
    e = g.readline().rstrip()   #Comment This to Reset Training Data
    e = list(map(int,e.split(',')))   #Comment This to Reset Training Data
    d[a] = e
m2 = moves(d)

#For Move4
d = {}
for i in range(252):
    a = f.readline().rstrip()
    a = tuple(map(int,a.split(',')))
    #b = set(a)   #Uncomment This to Reset Training Data
    #e = list(s-b)   #Uncomment This to Reset Training Data
    e = g.readline().rstrip()   #Comment This to Reset Training Data
    e = list(map(int,e.split(',')))   #Comment This to Reset Training Data
    d[a] = e
m4 = moves(d)

#For Move6
d = {}
for i in range(1260):
    a = f.readline().rstrip()
    a = tuple(map(int,a.split(',')))
    #b = set(a)   #Uncomment This to Reset Training Data
    #e = list(s-b)   #Uncomment This to Reset Training Data
    e = g.readline().rstrip()   #Comment This to Reset Training Data
    e = list(map(int,e.split(',')))   #Comment This to Reset Training Data
    d[a] = e
m6 = moves(d)

#For Move8
d = {}
for i in range(1260):
    a = f.readline().rstrip()
    a = tuple(map(int,a.split(',')))
    #b = set(a)   #Uncomment This to Reset Training Data
    #e = list(s-b)   #Uncomment This to Reset Training Data
    e = g.readline().rstrip()   #Comment This to Reset Training Data
    e = list(map(int,e.split(',')))   #Comment This to Reset Training Data
    d[a] = e
m8 = moves(d)

f.close()
g.close()

def writeback():
    g = open('T3_do.txt','w')
    for i in m2.m.values():
        for j in range(len(i)):
            i[j] = str(i[j])
        i = ','.join(i)
        g.write(i)
        g.write('\n')
    for i in m4.m.values():
        for j in range(len(i)):
            i[j] = str(i[j])
        i = ','.join(i)
        g.write(i)
        g.write('\n')
    for i in m6.m.values():
        for j in range(len(i)):
            i[j] = str(i[j])
        i = ','.join(i)
        g.write(i)
        g.write('\n')
    for i in m8.m.values():
        for j in range(len(i)):
            i[j] = str(i[j])
        i = ','.join(i)
        g.write(i)
        g.write('\n')

    g.close()
    
    global win_list
    h = open('T3_winratio.txt','a')
    for i in win_list:
        h.write(str(i)+',')
    
    h.close()

def stats():
    from matplotlib import pyplot as p
    h = open('T3_winratio.txt','r')
    
    x = h.read()[:-1]
    x = list(map(int,x.split(',')))
    N = len(x)
    for i in range(1,len(x)):
        x[i] += x[i-1]
    print('Number of Games Played:',N)
    print('Number of Games Tied/Won by CPU:',x[-1])
    p.plot(x)
    p.xlabel('Number of Games Played')
    p.ylabel('Number of Games Tied/Won by CPU')
    
    h.close()