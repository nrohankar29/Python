def result(n,m,a):
    b = [0]
    flag = 0
    top = 0
    for i in range(n):
        for j in range(flag+1):
            top += 1
            b.append(a[i] + b[j])
            flag = top
    if m in b:
        return("Yes")
    else:
        return("No")

for t in range(int(input())):
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(int(input()))
    print(result(n,m,a))