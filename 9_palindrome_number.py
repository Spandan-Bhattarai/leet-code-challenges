class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while(x>0):
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if(temp==rev):
            return 1
        else:
            return 0

#above code is only soluiton in leetcode
