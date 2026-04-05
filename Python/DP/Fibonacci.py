class solution:
    # Memoization Approach:
    # def fib(self,n,dp):
    #     if n<=1:
    #         return n
    #     if dp[n]!=-1:    #         return dp[n]
        
    #     dp[n]=self.fib(n-2,dp)+self.fib(n-1,dp)
    #     return dp[n]
    
    # #Tabulation Approach:
    # def fib(self,n):
    #     if n<=1:
    #         return n
    #     dp=[0]*(n+1)
    #     dp[0]=0
    #     dp[1]=1
    #     for i in range(2,n+1):
    #         dp[i]=dp[i-2]+dp[i-1]

    #     return dp[n]


    # Optimised Approach
    def fib(self,n):
        if n<=1:
            return n
        prev2=0
        prev=1
        for i in range(2,n+1):
            curr=prev2+prev
            prev2=prev
            prev=curr

        return prev
    
if __name__ == "__main__":
    n=8
    sol=solution()
    print(sol.fib(n))
