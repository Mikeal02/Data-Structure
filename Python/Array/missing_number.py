from operator import xor


class solution:
    # brute force: O(N^2)
    def missing_num(self,arr,N):
        for i in range(1,N+1):
            if i not in arr:
                return i

    # Optimal 1: O(n),O(1)
    
    def missing_num(self,arr,N):
        sum1=(N*(N+1)/2)
        for i in arr:
            sum2+=i

        return sum1-sum2

    # Optimal 2:O(N)
    def missing_num(self,arr,N):
        xor1,xor2=0,0
        for i in range(1,N+1):
            xor1^=i
        
        for i in arr:
            xor2^=i
        
        return xor1^xor2
        




if __name__=="__main__":
    arr=list((1,2,3,4,5,7))
    sol=solution()
    
    print(f"The missing number is {sol.missing_num(arr,7)}")