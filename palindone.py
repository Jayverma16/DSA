# palindrone with recursion 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        answer = True
        def check_palindrone(i,n,x):
            if i > n:
                return True
            if x[i] != x[n]:
                return False
            
            return check_palindrone(i+1,n-1,x)
        answer = check_palindrone(0,len(x)-1,x)
        return answer
            