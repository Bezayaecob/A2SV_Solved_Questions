t = int(input())
for _ in range(t):

    n = int(input())
    per_m = list(map(int, input().split()))
    ans = [per_m[0]]

    for i in range(1, n - 1):
        if (per_m[i] > per_m[i + 1] and per_m[i] > per_m[i - 1]) or (per_m[i] < per_m[i + 1] and per_m[i] < per_m[i - 1]):
            ans.append(per_m[i])

    ans.append(per_m[-1])

    print(len(ans))
    print(*ans)


