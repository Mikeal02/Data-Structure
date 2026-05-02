class solution:
    def ithsetbit(self,num,index):
        return num&(1<<index)!=0
sol=solution()
num=5
index=1
print(sol.ithsetbit(num,index))