#TIme --> o(number of words in input * length of the given word)
#space --> o(length of the given word)

class Solution:
    # generating a set of letters and list of word frequencies
    
    def word_dict(self,S):
        out=[]
        i=0
        
        while i<len(S):
            j=i
            count=0
            while j<len(S):
                if S[i]==S[j]:
                    count+=1
                else:
                    break
                j=j+1
            out.append(count)
            i=j      
            
        return set(S),out
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # for the input string S we create a set of the given unique words and a list of word frequencies
        main_keys,main_values=self.word_dict(S)
        
        ans=0
        
        for word in words:
            flag=False
            
            word_keys,word_values=self.word_dict(word)
            
            # checking for different words in given S and in words
            if main_keys!=word_keys:
                continue
            # checking the count of word freqiencies in both the word and the S.If the count of letter in S should not be less than 3    
            
            for c1,c2 in zip(main_values,word_values):
                if c1==c2:
                    continue
                elif c1<c2 or c1<3:
                    flag=True
            
            # flag==False means that the word has char with freqienies either equal to given or freq count in the given is >=3
            if flag==False:
                ans+=1
                
        return ans
                    