class Solution:
    def three_sum(self,arr):
        st=set()
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
                        st.add(triplet)

        return [list(triplet) for triplet in st]

if __name__=="__main__":
    arr=[-1,0,1,2,-1,-4]
    sol=Solution()
    result=sol.three_sum(arr)
    for triplet in result:
        print(triplet)



