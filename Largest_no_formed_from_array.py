def largest(n,l):
    for _ in range(n):
        
        for i in range(n-1):
            n1 = int(l[i]+l[i+1])
            n2 = int(l[i+1]+l[i])
            if n2 > n1:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    str1 = ''
    for st in l:
        str1 += st
    return str1

for _ in range(int(input())):
    n = int(input())
    l = input().split()
    print(largest(n,l))