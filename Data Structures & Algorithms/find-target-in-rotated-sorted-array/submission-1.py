class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l
        l, r = 0, len(nums) - 1
        if target <= nums[r] and target >= nums[pivot]:
            l = pivot
        else:
            r = pivot - 1

        while l < r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        if nums[l] == target:
            return l
        return -1