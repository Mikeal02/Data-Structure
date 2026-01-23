class Solution:
    def largest_odd_number(self,s:str)->str:
        ind=-1

        i=0
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2)==1:
                ind=i
                break

        i=0
        while i<=ind and s[i]=='0':
            i+=1

        return s[i:ind+1]

if __name__=="__main__":
    solution = Solution()
    num = "0214638"

    result = solution.largest_odd_number(num)
    print("Largest odd number:", result)