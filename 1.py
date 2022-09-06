#2 часа 20 минут
n = int(input())
l=[]
bludo = []
ingrid = [[] for i in range(n)]
decs_ingrid = []
decs_eat = []
for i in range(n):
    bludo.append(list(map(str, input().split())))
    bludo[i][1] = int(bludo[i][1])
    bludo[i][2] = int(bludo[i][2])
    for j in range(bludo[i][2]):
        ingrid[i].append(list(map(str, input().split())))
        ingrid[i][j][1] = int(ingrid[i][j][1])


k = int(input())
for kk in range(k):
    decs_ingrid.append(list(map(str, input().split())))
    decs_ingrid[kk][1] = int(decs_ingrid[kk][1])
    decs_ingrid[kk][2] = int(decs_ingrid[kk][2])

m = int(input())
for mm in range(m):
    decs_eat.append(list(map(str, input().split())))
    decs_eat[mm][1] = int(decs_eat[mm][1])
    decs_eat[mm][3] = float(decs_eat[mm][3])
    decs_eat[mm][4] = float(decs_eat[mm][4])
    decs_eat[mm][5] = float(decs_eat[mm][5])
    decs_eat[mm][6] = float(decs_eat[mm][6])
    

for i in range(n):
    for j in ingrid[i]:
        if j[2] == 'l':
            j[2] = 'ml'
            j[1]*=1000
        if j[2] == 'kg':
            j[2] = 'g'
            j[1]*=1000
        if j[2] == 'tens':
            j[2] = 'cnt'
            j[1]*=10

for kk in decs_ingrid:
    if kk[3] == 'l':
        kk[3] = 'ml'
        kk[2]*=1000
    if kk[3] == 'kg':
        kk[3] = 'g'
        kk[2]*=1000
    if kk[3] == 'tens':
        kk[3] = 'cnt'
        kk[2]*=10

for kk in decs_eat:
    if kk[2] == 'l':
        kk[2] = 'ml'
        kk[1]*=1000
    if kk[2] == 'kg':
        kk[2] = 'g'
        kk[1]*=1000
    if kk[2] == 'tens':
        kk[2] = 'cnt'
        kk[1]*=10

dict_ingrid = dict()
for i in range(n):
    for j in ingrid[i]:
        if j[0] in dict_ingrid:
            dict_ingrid[j[0]]+=j[1]*bludo[i][1]
        else:
            dict_ingrid[j[0]]=j[1]*bludo[i][1]


cost = 0
for kk in decs_ingrid:
    if kk[0] in dict_ingrid:
        tmp_res = dict_ingrid[kk[0]]//kk[2]
        # print(tmp_res, dict_ingrid[kk[0]], kk[2], kk[0])
        if dict_ingrid[kk[0]]%kk[2] == 0:
            dict_ingrid[kk[0]] = tmp_res
        else:
            dict_ingrid[kk[0]] = tmp_res + 1
        cost += dict_ingrid[kk[0]]*kk[1]
    else:
        dict_ingrid[kk[0]] = 0


list_info_bludo = [[0, 0, 0, 0] for i in range(n)]
for i in range(n):
    for j in ingrid[i]:
        for r in decs_eat:
            if j[0] == r[0]:
                nn = j[1]/r[1]
                list_info_bludo[i][0] += r[3]*nn
                list_info_bludo[i][1] += r[4]*nn
                list_info_bludo[i][2] += r[5]*nn
                list_info_bludo[i][3] += r[6]*nn

        

print(cost)
for key, val in dict_ingrid.items():
    print(key, val)
for i in range(n):
    print(bludo[i][0], *list_info_bludo[i])

