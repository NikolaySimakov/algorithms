class Solution:
    
    '''
    Solve using stack
    '''
    
    def removeOuterParentheses(self, s: str) -> str:
        temp = ''
        res = ''
        open_ = close_ = 0

        for i, c in enumerate(s):
            temp += c
            if c == '(':
                open_ += 1
            else:
                close_ += 1
        
            if open_ == close_:
                res += temp[1:-1]
                temp = ''
                open_ = 0
                close_ = 0

        
        return res