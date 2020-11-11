class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        curr = [nums[0]]
        glob = [nums[0]]

        for i in range(1, len(nums)):
            curr.append(max(nums[i], curr[i - 1] + nums[i]))
            glob.append(max(curr[i], glob[i - 1]))

        return glob[-1]
