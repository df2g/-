import random
def fun(a1,a2):#a1表示测试次数，a2表示池塘鸭子数量
 i = j = 0
 while (i < a1):
    a = []
    for t in range(a2):
        a.append(random.random())
    a.sort()
    if (a[a2 - 1] - a[0] < 0.5):
        j += 1
    else:
        check = []
        for t2 in range(a2 - 1):
            check.append(a[t2 + 1] - a[t2])
        check.sort()
        if (check[a2 - 2] > 0.5):
            j+=1
    i+=1
 return(j/i)
check=[]
for t0 in range(10):
    print(fun(10000,4))