#Time comp --> o(n)
#space comp --> o(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return '0'
        
        stack=[]
        
        for i in range(len(num)):
            if i==0:
                stack.append(num[i])
            elif num[i]>=stack[-1]:
                stack.append(num[i])
            else:
                while len(stack)>0 and num[i]<stack[-1] and k>0:
                    stack.pop()
                    k=k-1
                stack.append(num[i])
        # print(stack,k)
        
        while len(stack)>0 and k>0:
            stack.pop()
            k=k-1
            
        if ''.join(stack).lstrip('0')=='':
            return '0'
        return ''.join(stack).lstrip('0')
                