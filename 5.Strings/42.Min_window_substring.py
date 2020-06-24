#Time --> o(n)
#space -->o(n)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0 or len(t)==0:
            return ''
        dt = {}
        out=''
        mini = float('inf')
        #store the values of t in dict
        for i in t:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] = dt[i] + 1
        d = dict()
        start = 0
        end = 0
        # formed is to count the no of characters formed in the window to make it equal to T
        formed = 0
        # start and end pointers at the same initial position
        while end < len(s):
            # adding end element to the new string dictionary
            if s[end] in d:
                d[s[end]]=d[s[end]]+1
            else:
                d[s[end]]=1 
                
            # we check if the char is present in the main dict or not   
            if s[end] in dt and d[s[end]]<=dt[s[end]]:
                formed=formed+1
                
            # if the formed string is same as the string t then we see if from the start position if we can remove some characters to make it minimum
            
            if formed==len(t):
                while(s[start] not in dt or d[s[start]]>dt[s[start]]):
                    d[s[start]] = d[s[start]] - 1
                    start = start + 1
                    
                # storing the min string value and string 
                if mini>=end-start+1:
                    mini=min(mini,end-start+1)
                    out=s[start:end+1]
                    
            end=end+1
        if len(out)>0:
            return out
        else:
            return ""