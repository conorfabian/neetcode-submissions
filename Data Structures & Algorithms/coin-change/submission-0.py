class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0

        def dfs(val):
            if val in dp:
                return dp[val]
            elif val < 0:
                return float("inf")

            minCoins = float("inf")
            for coin in coins:
                minCoins = min(minCoins, dfs(val - coin))

            dp[val] = 1 + minCoins
            return dp[val]

        res = dfs(amount)
        if res == float("inf"):
            return -1
        return res