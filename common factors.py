m,n = map(int, input().strip().split(" "))
min_n = min(m,n)
count = 0
for i in range(1,int((min_n+1)/2)):
    if(m%i==0 and n%i==0):
        count+=1
if(m%n==0 or n%m==0):
    count+=1
print(count)        
