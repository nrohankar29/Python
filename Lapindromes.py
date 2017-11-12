def lapindrome(s):
    
    n = len(s)
    s1 = s[:n//2]
    if n % 2 == 0:
        s2 = s[n//2:]
    else:
        s2 = s[(n//2)+1:]
    
    for ch in set(s1):
        if s1.count(ch) != s2.count(ch):
            return("NO")
            break
    else:
        return("YES")
 
for t in range(int(input())):
    s = input()
    print(lapindrome(s)) 