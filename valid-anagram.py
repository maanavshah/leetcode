class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = 0
            hmap[s[i]] += 1
            if t[i] not in hmap:
                hmap[t[i]] = 0
            hmap[t[i]] -= 1

        return not any(v != 0 for v in hmap.values())
