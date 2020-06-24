#Time -->o(n*(m**2))
#m --> length of each word
#n--> total no of words in the input
#space  -->o(n*(m**2))
#m --> length of each word
#n--> total no of words in the input
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #if end word not in given input then we return 0
        if endWord not in wordList:
            return 0
        
        wordset=set()
        
        for val in wordList:
            wordset.add(val)
            
        queue=deque([[beginWord,0]])
        #visited dict for not going over the same thing and again
        visited=dict()
        visited[beginWord]=True
        
        while len(queue)>0:
            
            curr=queue.popleft()
            currword=curr[0]
            level=curr[1]
            
            if currword==endWord:
                return level+1
            
            for i in range(len(currword)):
                for j in range(26):
                    replaceword=chr(ord('a')+j)
                    #generating every word for eg:hit we generate words from [[a..z]it,h[a..z]t,hi[a..z]]
                    word1=currword[:i]+replaceword+currword[i+1:]
                    #checking if the generated word is in the given input or not
                    if word1 in wordset:
                        if word1 not in visited:
                            visited[word1]=True
                            queue.append([word1,level+1])
                            
        return 0
                    
            