class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        frequencies = [[] for i in range(len(nums))]
        for num, val in count.items():
            frequencies[val - 1].append(num)

        res = []
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
                else:
                    break

        return res