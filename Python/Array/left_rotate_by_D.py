class solution:
    # optimal solution: O(n),O(1)

    def reverse(self,arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    def left_rotate_by_D(self,arr,k,direction):
        n=len(arr)
        k%=n
        if n==0 or k==0:
            return
        
        if direction=="left":
            self.reverse(arr,0,k-1)
            self.reverse(arr,k,n-1)
            self.reverse(arr,0,n-1)
        else:
            self.reverse(arr,0,n-1)
            self.reverse(arr,0,k-1)
            self.reverse(arr,k,n-1)
            
if __name__ == "__main__":
    sol=solution()
    n=int(input())
    dir=input()
    arr=list(range(1,9))
    sol.left_rotate_by_D(arr,n,dir)
    print(arr)
   
