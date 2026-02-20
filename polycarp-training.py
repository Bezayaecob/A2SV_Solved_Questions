x= int(input())
y= list(map(int, input().split()))
y.sort()
days=1
res=0
for i in range(0,x):
    if y[i] >=days:
        days+=1
        res+=1
print(res)
