class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1

        return res