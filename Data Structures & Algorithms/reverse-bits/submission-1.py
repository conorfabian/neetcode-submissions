class Solution:
    def reverseBits(self, n: int) -> int:
        binary = [bin(n)[2:][::-1]]

        while len(binary[0]) + len(binary[1:]) < 32:
            binary.append("0")

        num = "".join(binary)

        res = 0
        exp = 0
        for i in range(len(num) - 1, -1 , -1):
            res += int(num[i]) * (2 ** exp)
            exp += 1

        return res