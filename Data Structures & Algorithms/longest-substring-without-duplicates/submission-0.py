class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l, r = 0, 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res