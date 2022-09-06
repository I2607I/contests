def pr(n):
   i = 2
   prl = []
   while i * i <= n:
       while n % i == 0:
           prl.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       prl.append(n)
   return prl




a = list(map(int, input().split()))
n1 = a[0]
n2 = a[1]

# l1 = list(set(pr(n1)))
# l2 = list(set(pr(n2)))
l1 = pr(n1)
l2 = pr(n2)
# print(l1, l2)
count = 0
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l1[i] = 0
            l2[j] = 0
            count+=1
            break

if n1 != n2:
    if n1 == 1 or n2 == 1:
        print(2)
    else:
        print(count*2)
else:
    if n1 == 1:
        print(1)
    else:
        print(1)



# a = 9486
# print(pr(a))