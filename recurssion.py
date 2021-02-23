def duplicate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(*b)


a = list(map(int, input().split()))

duplicate(a)
