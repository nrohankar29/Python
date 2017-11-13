#!/bin/python3

import sys

def bestbuy(d):
    
    d2 = {}
    
    for key in d:
        
        c1 = d[key].count('4')
        c2 = d[key].count('7')
        
        if c1 == c2 and len(d[key]) == c1+c2:
            d2[key] = d[key]
    if len(d2) == 1:
        for i in d2.keys():
            return(i)
    elif len(d2) == 0:
        return -1
    elif len(d2) > 1:
        l = []
        for j in d2.values():
            l.append(int(j))
        m = min(l)
        m = str(m)
        for key,value in d2.items():
            if value == m:
                return key
d = {}
if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        s, n = input().strip().split(' ')
        s, n = [str(s), str(n)]
        d[s] = n
print(bestbuy(d))