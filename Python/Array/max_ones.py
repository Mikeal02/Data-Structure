# optimal solution: O(n)
def max_ones(arr):
    n=len(arr)
    count=0
    maxones=-1
    for i in range(n):
        if arr[i]==1:
            count=count+1
            maxones=max(maxones,count)

        else:
            count=0
    
    return maxones




if __name__ == "__main__":
    arr=[0,0,1,0,1,1,1,1,0,1,1]
    maxones=max_ones(arr)
    print(f"The maximum consecutive ones are {maxones}")