#Time --> o(mn)
#space  -->o(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m=len(num1)
        n=len(num2)
        out=[0 for i in range(m+n)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                val=(ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                p1=i+j
                p2=i+j+1
                sum1=val+out[p2]
                out[p1]+=sum1//10
                out[p2]=sum1%10
                # print(out)
        res=''    
        for val in out:
            res=res+str(val)
        
        if len(res.lstrip("0"))==0:
            return "0"
        else:
            return res.lstrip("0")