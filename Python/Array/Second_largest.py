arr=[2,3,4,5,22,65,23,12,53,65,75]
# // brute force solution: O(nlogn)
def second_element(arr):
    arr.sort()
    return arr[len(arr)-2]


# Optimal solution:O(n)
def second_element(arr):
    maxi=arr[0]
    maxi2=-1
    for i in range(2,len(arr)):
        if arr[i]>maxi:
            maxi2=maxi
            maxi=arr[i]

        elif arr[i]<maxi and arr[i]>maxi2:
            maxi2=arr[i]

    return maxi2

second_largest=second_element(arr)
print(f"The largest element is {second_largest}")