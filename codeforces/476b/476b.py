s1 = input()
s2= input()
val = 0
for i in range(len(s1)):
    if s1[i] == '+':
        val += 1
    else:
        val -= 1

res = []
def recurse(curr, n):
    if n == len(s1):
        res.append(curr)
        return
    if s2[n] == '+':
        recurse(curr+1, n+1)
    elif s2[n] == '-':
        recurse(curr-1, n+1)
    else:
        recurse(curr-1, n+1)
        recurse(curr+1, n+1)
recurse(0, 0)
ans = res.count(val)
print((ans/len(res)))