for _ in range(int(input())):
    n = int(input())
    s = input()


    possible_values = ["aa", "aba", "aca", "abca", "acba", "abbacca", "accabba"]
    
    for value in possible_values:
        if value in s:
            print(len(value))
            break
        
    else:
        print(-1)