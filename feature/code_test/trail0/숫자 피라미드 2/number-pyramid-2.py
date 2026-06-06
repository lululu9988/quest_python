n=int(input())
ans=0

for i in range(n):
    for j in range(i+1):
        ans+=1
        print(ans,end=" ")
    print() 