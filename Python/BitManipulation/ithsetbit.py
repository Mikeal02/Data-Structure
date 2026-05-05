class solution:

    # brute force solution:
    def ithsetbit(self,num,index):
        binary=bin(num)[2:]
        if index>=len(binary):
            return False
        
        return binary[-(index+1)]=='1'

    # def ithsetbit(self,num,index):
    #     return num&(1<<index)!=0

        
sol=solution()
num=5
index=1
print(sol.ithsetbit(num,index))