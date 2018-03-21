m=0
n=0
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
        
x = ack(3,4)                                  # RecursionError: maximum recursion depth exceeded
                                                      #in comparison for large values of m and n
print(x)

