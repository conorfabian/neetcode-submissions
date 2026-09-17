class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            temp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            res = max(res, currMax)

        return res