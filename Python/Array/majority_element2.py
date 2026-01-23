from collections import defaultdict


class Solution:
    # brute force approach:O(n^2)
    def majority_element(self,arr):
        n=len(arr)
        for x in arr:
            count=0
            for y in arr:
                if x==y:
                    count+=1
            
            if count>(n/2):
                return x
        return -1

    # better approach:O(n) [Using hashmap/dictionary]
    def majority_element(self,arr):
        n=len(arr)
        freq=defaultdict(int)
        for x in arr:
            freq[x]+=1

        for x,y in freq.items():
            if y>(n/2):
                return x
        return -1

    def majority_element(self,arr):
        n=len(arr)
        count=0
        ele=0
        for x in arr:
            if count==0:
                count+=1
                ele=x
            
            elif ele==x:
                count+=1

            else:
                count-=1

        count1=0
        for x in arr:
            if x==ele:
                count1+=1
            
        if count1>(n/2):
            return ele

        return -1


if __name__=="__main__":
    arr=[7,0,0,1,7,7,2,7,7]
    sol=Solution()
    ans=sol.majority_element(arr)
    print(f"The majority element with occurence greater than N/2 is {ans}")