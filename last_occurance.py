def last_occurance(arr,ele):
    
    for i in range(len(arr)-1,-1,-1):
        
        if arr[i] == ele:
            
            return i+1

    return (-1)
            
t = list(map(int,input().split(' ')))

ele = t[1]

arr = list(map(int,input().split(' ')))

print(last_occurance(arr,ele))
