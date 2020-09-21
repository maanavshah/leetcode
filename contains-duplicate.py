class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter:
                return True
            counter[nums[i]] = 1
        return False

        # return len(nums) != len(set(nums))
