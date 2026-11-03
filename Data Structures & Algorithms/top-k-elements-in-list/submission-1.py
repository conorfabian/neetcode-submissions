class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        frequencies = [[] for _ in range(len(nums) + 1)]
        for val, count in counts.items():
            frequencies[count].append(val)

        res = []
        for i in range(len(frequencies) - 1, -1, -1):
            for val in frequencies[i]:
                if k == 0:
                    break
                res.append(val)
                k -= 1

        return res