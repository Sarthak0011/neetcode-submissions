class Solution:
    def solve(self, n: int, dp: List[int]) -> int:
        if n == 0 or n == 1:
            dp[n] = 1
            return 1
        
        if dp[n] != -1:
            return dp[n]

        one_step = self.solve(n-1, dp)
        two_step = self.solve(n-2, dp)

        dp[n] = one_step + two_step
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        self.solve(n, dp)
        return dp[n]