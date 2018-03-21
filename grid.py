#Ex 7 Grid
def grid(r,c):
    for i in range(0,r):
        for j in range(0,c):
            if i==0 or i==int(r/2) or i==r-1:
                if j==0 or j==int(c/2) or j==c-1:
                    print("+", end=' ')
                else:
                    print("-", end=' ')
            elif j==int(c/2) or j==0 or j==c-1:
                print("|", end=' ')
            else:
                print(" ", end=' ')
        print()
grid(11,11)
