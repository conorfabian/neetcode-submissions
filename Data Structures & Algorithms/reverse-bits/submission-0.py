class Solution:
    def reverseBits(self, n: int) -> int:
        num = [bin(n)[2:][::-1]]

        length, count = len(num[0]), 0
        while length + count < 32:
            num.append('0')
            count += 1

        num = "".join(num)[::-1]
        
        res = 0
        for i in range(31, -1, -1):
            res += 2 ** i * int(num[i])

        return res