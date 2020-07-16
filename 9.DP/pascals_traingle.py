#Time comp -->> o(n2)
#space comp --> o(n20

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==0:
            return []
        
        out=[[1]]
        
        
        
        for i in range(1,numRows):
            prev=out[-1]
            list1=[None for i in range(i+1)]
            list1[0]=1
            list1[i]=1
            
            for j in range(len(prev)-1):
                list1[j+1]=prev[j]+prev[j+1]
                
            out.append(list1)
            
        return out
        
        
            
        
            
                
            
        