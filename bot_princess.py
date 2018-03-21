#!/usr/bin/pyth
def displayPathtoPrincess(n,grid):
    #print all the moves here
    count = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for i in range(0,m):
        for j in range(0,m):
            while(count!=2):
                if(grid[i][j]=='m'):
                    x1=i
                    y1=j
                    count+=1
                elif(grid[i][j]=='p'):
                    x2=i
                    y2=j
                    count+=1
    while(x2!=x1):
        if((x2-x1)>0):
            print("RIGHT\n")
            x1+=1
        elif((x2-x1)<0):
            print("LEFT\n")
            x1-=x1
    while(y2!=y1):
        if((y2-y1)>0):
            print("UP\n")
            y1+=1
        elif((y2-y1)<0):
            print("DOWN\n")
            y1-=y1
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
