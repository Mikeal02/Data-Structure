
from collections import defaultdict


class Solution:
    # def repeat_missing(self,arr):
    #     freq={}
    #     repeating=-1
    #     missing=-1
        
    #     for i in range(len(arr)):
    #         freq[arr[i]]=freq.get(arr[i],0)+1
    #         if freq[arr[i]]==2:
    #             repeating=arr[i]

    #     for i in range(1,len(arr)+1):
    #         if i not in freq:
    #             missing=i
    #             break

    #     return repeating,missing


    def repeat_missing(self, arr):
        n=len(arr)
        s,sn=0,0
        s2=(n*(n+1))//2
        s2n=(n*(n+1)*(2*n+1))//6

        for i in range(n):
            s+=arr[i]
            sn+=(arr[i]**2)

        val1=s2-s
        val2=s2n-sn

        val2=val2//val1

        x=(val1+val2)//2
        y=x-val1

        return x,y


if __name__=="__main__":
    arr=[3, 1, 2, 5, 4, 6, 7, 5]
    sol=Solution()
    a,b=sol.repeat_missing(arr)
    print(f"The repeating number is {a} and the missing number is {b}")
