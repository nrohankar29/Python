def solve(m,index,b):
    if m == 0:
        return True
    elif index == len(b) or m < 0:
        return False
    return solve(m-b[index],index+1,b) or solve(m,index+1,b)

for _ in range(int(input())):
    n,m = map(int,input().split())
    b = [int(input()) for _ in range(n)]
    if solve(m,0,b):
        print("Yes")
    else:
        print("No")