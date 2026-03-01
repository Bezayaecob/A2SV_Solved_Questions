from collections import Counter

for _ in range(int(input())):
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)

    counter_s = Counter(s)
    counter_t = Counter(t)

    for ch, count in counter_s.items():
        if counter_t[ch] < count:
            print("Impossible")
            break
    else:
        leftover = []
        for ch, count in (counter_t - counter_s).items():
            leftover.extend([ch] * count)
        leftover.sort()

        answer = []
        i = j = 0
        while i < s_len and j < len(leftover):
            if s[i] <= leftover[j]:
                answer.append(s[i])
                i += 1
            else:
                answer.append(leftover[j])
                j += 1
        answer.extend(s[i:])
        answer.extend(leftover[j:])

        print("".join(answer))
