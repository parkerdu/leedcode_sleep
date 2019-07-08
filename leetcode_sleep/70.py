class Solution:
    def climbStairs(self, n: int) -> int:
        """dfs方法：时间2^n"""
        if not n:
            return
        self.res = 0
        self.dfs(n)
        return self.res

    def dfs(self,n):
        if not n:
            self.res += 1
        if 0< n < 2:
            self.dfs(n-1)
        elif n >= 2:
            self.dfs(n-1)
            self.dfs(n-2)

    def climbStairs1(self, n: int) -> int:
        """动态规划，O(N)时间，O(N)空间"""
        if not n:
            return
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        """动态规划，O(N)时间，O(1)空间"""
        if not n:
            return
        dp = 1
        num_of_ones = 1
        for i in range(n-1):
            dp, num_of_ones = dp+num_of_ones,dp
        return dp

if __name__ == "__main__":
    su = Solution()
    print(su.climbStairs2(4))