class Solution:
    def countDuplicates(self, arr: List[int]) -> int:

        if len(arr) < 2:
            return 0
        keys = {}
        count = 0
        for x in arr:
            if keys.get(x):
                count += 1
            else:
                keys[x] = 1
        return count
