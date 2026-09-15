class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            elif i >= len(s):
                dp[i] = 1
                return dp[i]
            elif s[i] == "0":
                dp[i] = 0
                return dp[i]

            res = dfs(i + 1)
            if i + 1 < len(s) and ((s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res
            return dp[i]

        return dfs(0)