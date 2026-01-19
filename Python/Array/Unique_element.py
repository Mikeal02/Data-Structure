# Problem Statement: Given a non empty array of integers arr, every element appears twice except for one. Find that single one 

class solution:
    # Brute force:O(n*n) [we count every element in the array and return the one with count 1]
    # def unique_num(self,arr):
    #     for i in arr:
    #         for j in arr:
    #             count=0
    #             if i==j:
    #                 count+=1
    #             if count==1:
    #                 return i

    # Better solution:O(n),O(n)  [we will use hashmap]
    # def unique_num(self,arr):
    #     hashmap={}
    #     for i in arr:
    #         if i in hashmap:
    #             hashmap[i]+=1
    #         else:
    #             hashmap[i]=1
        
    #     for i in hashmap:
    #         if hashmap[i]==1:
    #             return i

    # Optimal 1:O(n) [we use xor property x^x=0]
    def unique_num(self,arr):
        ans=0
        for i in arr:
            ans^=i
        return ans





if __name__=="__main__":
    arr=list((4,1,2,1,2,4,3,11,5,3,5))
    sol=solution()
    
    print(f"The unique number is {sol.unique_num(arr)}")