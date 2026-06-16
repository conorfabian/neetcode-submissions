class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f"{len(s)}")
            res.append(",")
            res.append(s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != ',' and j < len(s) - 1:
                j += 1
            size = int(s[i:j]) + 1
            res.append(s[j+1:j+size])
            i = j + size

        return res