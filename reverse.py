# Question # https://leetcode.com/problems/reverse-integer/

def reverse( x: int) -> int:
    
    sign = 1
    if (x<0):
        x = -1*x
        sign = -1
    
    # reminder = []
    reverse = 0
    count = 0
    while(x>0):
        reminder = x%10
        # print(reminder)
        reverse = reverse*10 + reminder
        # print(reverse)
        x=int(x/10)
        count+=1
    max = pow(2,31) -1
    min =  -1* (max+1)
    if min <= reverse *sign <= max:
        return reverse *sign
    else:
        return 0

print(reverse(-49494))
print(reverse(408))
print(reverse(500))
print(reverse(1534236469))
# print(pow(2,31))

