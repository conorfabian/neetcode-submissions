class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(start, end):
            if s[start:end + 1] in dp:
                return dp[s[start:end + 1]]
            elif end + 1 == len(s) and s[start:]:
                dp[s[start:]] = s[start:] in wordDict
                return dp[s[start:]]
            elif s[start:end + 1] in wordDict:
                dp[s[start:end + 1]] = dfs(end + 1, end + 1) or dfs(start, end + 1)
                return dp[s[start:end + 1]]

            dp[s[start:end + 1]] = dfs(start, end + 1)
            return dp[s[start:end + 1]]

        return dfs(0, 0)