def middle(x):
    x.remove(x[0])
    i=len(x)-1
    x.remove(x[i])
    return x

def input_list(x,n):
    "Takes the input from the user for the list elements"
    for i in range(0,n):
        x.append(input())

x=[]
n=int(input("Enter number of elements "))
input_list(x,n)
middle(x)
print(x)

    
