#https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        flag=0
        t=s
        if s[0]=="-":
            t=s[1:]
            x=int(t)
            flag=1
        temp=0
        while x>0:
            r=x%10
            temp=(10*temp)+r
            x=x//10
        if flag==1:
            if -1*temp<-2**(31):
                return 0
            return -1*temp
        else:
            if temp>(2**(31))+1:
                return 0
            return temp

a=int(input())
ob=Solution()
print(ob.reverse(a))