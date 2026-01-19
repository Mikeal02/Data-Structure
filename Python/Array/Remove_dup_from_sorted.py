# Brute Force Solution: O(1), O(n)
def remove_dup(arr):
    arr2=set(arr)
    return len(arr2)

# Optimal Solution: O(n)
def remove_dup(arr):
    if len(arr)==0:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        
    return i+1


arr=[1,1,2,2,2,3,3]
ans=remove_dup(arr)
print(ans)