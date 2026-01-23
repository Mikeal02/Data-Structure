class Solution:
    def reverse_words(self,s):
        n=len(s)
        result=""
        i=n-1
        while i>=0:
            while i>=0 and s[i]==' ':
                i-=1

            end=i
            while i>=0 and s[i]!=' ':
                i-=1;
            
            word=s[i+1:end+1]

            if result!="":
                result+=' '
            result+=word

        return result

if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverse_words(s))
