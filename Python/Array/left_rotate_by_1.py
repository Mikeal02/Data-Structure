class solution:
    # optimal solution: O(n),O(1)
    def left_rotate(self,arr):
        first_element=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=first_element


if __name__ == "__main__":
    sol=solution()
    arr=list(range(1,9))
    sol.left_rotate(arr)
    print(arr)

