#Time comp --> o(n2)
#space comp --> o(n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        out=[1 for i in range(rowIndex+1)]

        for i in range(rowIndex+1):
            count=i
            
            while count>0:
                
                out[count]=out[count]+out[count-1]
                count=count-1
            out[i]=1
        return out
            
            
                
                
        