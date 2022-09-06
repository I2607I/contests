n = list(map(int, input().split()))

lst = list(map(int, input().split()))
lst = [0] + lst
for i in range(n[2]):
    f = 1
    p = list(map(int, input().split()))
    for j in lst[p[2]:p[3]+1]:
        # print('j', j)
        if j != p[0]:
            f = 0
            break
    # print('p', p)
    # print('lst', lst)
    if f == 1:
        for j in range(p[2], p[3]+1):
            lst[j] = p[1]
    

    print(f)




