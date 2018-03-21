def cumsum(x):
    for i in range(len(x)):
        sum=0
        for j in range(0,i+1):
            sum=sum+x[j]
        y.append(sum)
    return y

def input_list(x,n):
    "Takes the input from the user for the list elements"
    for i in range(0,n):
        x.append(int(input()))

x=[]
n=int(input("Enter number of elements "))
input_list(x,n)
y=[]
y=cumsum(x)
print(y)
    
