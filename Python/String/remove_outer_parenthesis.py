class Solution:
    def remove_outer_parenthesis(self,s):
        result=""
        level=0
        for c in s:
            if c=='(':
                if level>0:
                    result+=c
                level+=1

            elif c==')':
                level-=1
                if level>0:
                    result+=c
                    
        return result

if __name__=="__main__":
    s="(()())(())"
    sol=Solution()
    result=sol.remove_outer_parenthesis(s)
    print(result)