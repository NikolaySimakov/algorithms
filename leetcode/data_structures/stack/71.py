class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            p = p.replace('/', '')
            if p == '.' or not p:
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)