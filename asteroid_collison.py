#Time comp --> o(n)
#space comp --> o(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        for val in asteroids:
            # if the asteroid value is +ve
            if val>0:
                stack.append(val)
            else:
                # the top element should be positive and the coming asteroid should be -ve then only we see some collision to pick the largest one
                while len(stack)>0 and stack[-1]>0:
                    # if the value at the top is having less value than the incoming astreiod then the top asteroid will be crushed
                    if stack[-1]<abs(val):
                        stack.pop()
                        continue
                    # when both the asteroids have the same value then we crush both of them
                    elif stack[-1]==abs(val):
                        stack.pop()
                        break
                        
                    else:
                        break
                # if the top element is not +ve or if stack is not empty we add it to the stack
                else:
                    stack.append(val)
        return stack
                         