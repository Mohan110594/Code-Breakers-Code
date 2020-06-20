#Time comp --> o(n*k) n-->input length and k--> number of indices which are having more gas than cost.
#space comp -->o(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startindex=[]
        for i in range(len(gas)):
            if gas[i]>=cost[i]:
                startindex.append(i)
        
        for start in startindex:
            cartank=0
            # print(start)
            for j in range(start,len(gas)):
                if cartank<0:
                    break
                cartank+=gas[j]-cost[j]
            
            p=0
            while p!=start:
                if cartank<0:
                    break
                cartank+=gas[p]-cost[p]
                p=p+1
                

            if cartank>=0 and j==len(gas)-1 and p==start:
                return start
            
        return -1
        
        
o(n) solution:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start=0
        total_cost=0
        current_cost=0
        for i in range(len(gas)):
            total_cost+=gas[i]-cost[i]
            current_cost+=gas[i]-cost[i]
            
            if  current_cost<0:
                start=i+1
                current_cost=0
        
        if total_cost<0:
            return -1
        else:
            return start
        