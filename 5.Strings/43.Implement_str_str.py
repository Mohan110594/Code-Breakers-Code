#Time --> o(m+n)
#space --> o(n)
#KMP Algorithm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        n=len(needle)
        
        pattern=[0 for i in range(n)]
        
        j=0
        i=1
        
        # pattern array creation
        while i<n:
            # print(i,j,pattern)
            if needle[j]==needle[i]:
                pattern[i]=j+1
                j+=1
                i+=1
            else:
                if j==0:
                    pattern[i]=0
                    i=i+1
                else:
                    j=pattern[j-1]
        
        
        h_index=0
        n_index=0
        
        # using generated pattern matrix to get the first occurence of needle in haystack
        while h_index<len(haystack) and n_index<len(needle):
            
            if haystack[h_index]==needle[n_index]:
                h_index+=1
                n_index+=1
                if n_index==len(needle):
                    return h_index-n_index
            else:
                if n_index==0:
                    h_index+=1
                else:
                    n_index=pattern[n_index-1]
                
        return -1
                
                
                
            
            
            
            
            
            