#Justin Butler 10/4/2021
class Solution(object):
    def climbStairs(self, n):
        dp = [1, 1] # Handle the first 2 Dynamic Programming cases
        for i in range(2, n+1): # Handle the remaining DP cases
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
