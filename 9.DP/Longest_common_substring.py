#DP

#Time complexity --> o(mn)
#space complexity --> o(n)

def find_LCS_length(s1, s2):
  dp=[0 for i in range(len(s2)+1)]
  maxlen=float('-inf')
  for i in range(len(s1)):
    for j in range(len(s2)-1,-1,-1):
      if s2[j]==s1[i]:
        dp[j+1]=1+dp[j]
        maxlen=max(maxlen,dp[j+1])
      else:
        dp[j+1]=0

    print(dp)
  return maxlen

#DP

#Time comp --> o(mn)
#space comp --> o(mn)

def find_LCS_length(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
        maxLength = max(maxLength, dp[i][j])
  return maxLength




