class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def delete(self):
        del self.items[len(self.items)-1]
        
    def maxele(self):
        return max(self.items)
s = Stack()
N = int(input().strip())
for i in range(N):
    l = list(map(int,input().strip().split(' ')))
    if l[0] == 1:
        s.push(l[1])
    elif l[0] == 2:
        s.delete()
    elif l[0] == 3:
        print(s.maxele())