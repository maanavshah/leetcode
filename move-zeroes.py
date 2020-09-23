class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_zero_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_zero_at] = nums[last_zero_at], nums[i]
                last_zero_at += 1

        return nums
