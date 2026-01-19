
# // brute force solution: O(nlogn)
def maxelement(arr):
    arr.sort()
    return arr[len(arr)-1]

# Optimal solution:O(n)
def maxelement(arr):
    n=len(arr)
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]

    return maxi

if __name__ =="__main__":
    arr=[2,3,4,5,22,65,23,12,53,65,75]
    largest=maxelement(arr)
    print(f"The largest element is {largest}")