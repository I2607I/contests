x, y = map(int, input().split())

if y % x != 0:
    print(0)
else:
    y //= x

    i = 2
    ans = 0
    while i * i <= y:
        if y % i == 0:
            ans += 1
            while y % i == 0:
                y //= i
        i += 1

    if y != 1:
        ans += 1

    print(2 ** ans)


