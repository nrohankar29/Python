def Gautam_search(length,position,Gautam_time):
    
    Total_time = 0
    
    i = 1
    
    while i <= position:
        
        Total_time += Gautam_time
        i += 1
            
    return(Total_time)
    
def Subhash_search(length,position,Subhash_time):
    
    Total_time = 0
    
    low = 1
    high = length
    
    while low <= high:
        
        mid = low + ((high - low)//2)
        
        if mid == position:
            
            Total_time += Subhash_time
            return Total_time
            
        if mid < position:
            
            low = mid + 1
            Total_time += Subhash_time
            
        else:
            
            high = mid - 1
            Total_time += Subhash_time
    


t = int(input())

for i in range(t):
    
    l = list(map(int,input().split(' ')))
    Gautam = Gautam_search(l[0],l[1],l[2])
    Subhash = Subhash_search(l[0],l[1],l[3])
    if Subhash < Gautam:
        print('2')
    if Subhash > Gautam:
        print('1')
    if Subhash == Gautam:
        print('0')