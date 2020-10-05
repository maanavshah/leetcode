class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            min_iter = min(len(prefix), len(strs[i]))
            prefix = prefix[:min_iter]
            for j in range(min_iter):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    if not prefix:
                        return ''
                    break
        return prefix
