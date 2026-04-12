import bisect

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    prev = -10**18
    possible = True
    
    for i in range(n):
        res = float('inf')
        
       
        if a[i] >= prev:
            res = a[i]
        
       
        target = prev + a[i]
        idx = bisect.bisect_left(b, target)
        
        if idx < m:
            val = b[idx] - a[i]
            if val >= prev:
                res = min(res, val)
        
        if res == float('inf'):
            possible = False
            break
        
        prev = res
    
    print("YES" if possible else "NO")