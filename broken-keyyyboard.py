from collections import Counter 
t= int(input())
for _ in range(t):
    s= input()
    res= set()
    i=0
    while i < len(s)-1:
        if s[i] !=s[i+1]:
            res.add(s[i])
            i+=1
        else:
            i+=2
    if i == len(s)-1:
        res.add(s[-1])
    ans= list(res)   
    print("".join(sorted(ans)))
    
