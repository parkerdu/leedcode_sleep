class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(1,n):
            dp[i] = dp[i-1] * (1-obstacleGrid[0][i])
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] * (1-obstacleGrid[i][j])
                else:
                    dp[j] = (dp[j-1] + dp[j])*(1-obstacleGrid[i][j])
        return dp[-1]

if __name__ == "__main__":
    a = [
  [0,1,0],
  [0,1,0],
  [0,0,0]
]
    su = Solution()
    print(su.uniquePathsWithObstacles(a))
