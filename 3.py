import sys
n =int(sys.stdin.readline())
for i in range(n):
    l = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    mn = lst[0] ^ lst[1]
    for j in range(l - 1):
            mn = min(lst[j] ^ lst[j+1], mn)

    print(mn)

