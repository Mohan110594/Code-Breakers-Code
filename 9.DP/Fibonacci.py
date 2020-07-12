#Time cmp -->o(n)
#space -> o(n)

class Solution:
    def fib(self, N: int) -> int:
        
        if N==0:
            return 0
        fib=[0 for i in range(N+1)]
        
        fib[1]=1
        
        for i in range(2,N+1):
            fib[i]=fib[i-1]+fib[i-2]
            
        return fib[len(fib)-1]