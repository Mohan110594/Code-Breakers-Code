# Time complexity --> o(n)
# space complexity --> o(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for val in tokens:
            if val!='+' and val!='-' and val!='*' and val!='/':
                stack.append(val)
            else:
                val1=int(stack.pop())
                val2=int(stack.pop())
                # print(val1,val2)
                if val=='+':
                    stack.append(val1+val2)
                elif val=='-':
                    stack.append(val2-val1)
                elif val=='*':
                    stack.append(val1*val2)
                else:
                    stack.append(int(val2/val1))
        return stack[0]
        
        