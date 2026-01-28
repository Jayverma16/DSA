from typing import List

def generateParenthesis(n: int) -> List[str]:
    result = []
    def bracket(left_close , right_close, res):
        if len(res) == 2*n:
            result.append(res)
            return  
        if left_close<n:
            bracket(left_close +1 , right_close, res + "(")
        if right_close<left_close:
            bracket(left_close , right_close +1, res + ")")


    bracket(0,0,"") 

    return result


if __name__== "__main__":
    n = 3
    Output=["((()))","(()())","(())()","()(())","()()()"]
    if Output == generateParenthesis(n):
        print("test case pass")
    else:
        print(generateParenthesis(n))