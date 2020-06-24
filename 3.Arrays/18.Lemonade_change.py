Time comp --> o(n)
space comp --> o(1)
1.Maintain the count of 5s,10s and 20s.
2.Then change accordingly.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        tens=0
        twenty=0
        for val in bills:
            if val==5:
                five+=1
            elif val==10:
                if five>0:
                    five=five-1
                else:
                    return False
                tens+=1
            else:
                if tens>0 and five>0:
                    tens-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
                twenty+=1
        return True
                    