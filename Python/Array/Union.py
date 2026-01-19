from collections import defaultdict
class Solution:
    # Better approach 2: O((m+n)log(m+n)), O(m+n) [Using map/dict]
    # def union_array(self,arr1,arr2):
    #     
    #     freq=defaultdict(int)
    #     for i in arr1:
    #         freq[i]+=1
        
    #     for j in arr2:
    #         freq[j]+=1
        
    #     ans=list()
    #     for x,y in freq.items():
    #         ans.append(x)
        
    #     return ans
    
    #  Better approach 2: O((m+n)),O(m+n) [Using set, cause in python set is hash table which insertion take O(1)]
    # def union_array(self,arr1,arr2):
    #     temp=set()
    #     ans=list()
    #     for i in arr1:
    #         temp.add(i)

    #     for j in arr2:
    #         temp.add(j)

    #     for x in temp:
    #         ans.append(x)
        
    #     return ans
    
    # optimal approach: O(n+m),O(n+m) 
    def union_array(self,arr1,arr2):
        n=len(arr1)
        m=len(arr2)
        ans=list()
        i,j=0,0
        while i<n and j<m:
            if arr1[i]==arr2[j]:
                if not ans or ans[-1]!=arr1[i]:
                    ans.append(arr1[i])
                i+=1
                j+=1

            elif arr1[i]<arr2[j]:
                if not ans or ans[-1]!=arr1[i]:
                    ans.append(arr1[i])
                i+=1

            elif arr2[j]<arr1[i]:
                if not ans or ans[-1]!=arr2[j]:
                    ans.append(arr2[j])
                j+=1

        while i<n:
            if not ans or ans[-1]!=arr1[i]:
                    ans.append(arr1[i])
            i+=1
            
        while j<m:
            if not ans or ans[-1]!=arr2[j]:
                    ans.append(arr2[j])
            j+=1

        return ans


if __name__=="__main__":
    arr1=[1,2,3,4,5,6]
    arr2=[2,4,6,8,9]

    sol=Solution()
    ans=sol.union_array(arr1,arr2)
    print(ans)