#Time comp --> o(mn)
#space comp --> o(mn)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        out=[[None for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if i==0:
                    if j==0:
                        out[i][j]=1
                    else:
                        out[i][j]=0
                else:
                    if coins[i-1]>j:
                        out[i][j]=out[i-1][j]
                    else:
                        out[i][j]=out[i-1][j]+out[i][j-coins[i-1]]
        return out[len(coins)][amount]
                