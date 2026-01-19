# Brute Force Solution: O(nlogn)
def is_sort(arr):
    if arr==sorted(arr):
        return True
    else:
        return False

# Optimal Solution: O(n)
def is_sort(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
        else :
            continue
    return True

arr=[1,2,3,4,5]
print(is_sort(arr))
    