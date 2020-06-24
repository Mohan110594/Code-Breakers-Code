#Time --> o(n**2)
#space --> o(1)
class Solution:
    def isValid(self, S: str) -> bool:
        n=len(S)
        for i in range(n):
            S=S.replace("abc",'')
        if len(S)==0:
            return True
        return False
        
        
with stack:
#Time --> o(n)
#space --> o(n)
class Solution:
    def isValid(self, S: str) -> bool:
        stack=[]
        for val in S:
            if val=='c' and len(stack)>=2:
                if (stack[-1]!='b' or stack[-2]!='a'):
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(val)
        return len(stack)==0
        