class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        currMax, currMin = 1, 1
        for num in nums:
            temp = num * currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            res = max(res, currMax)

        return res