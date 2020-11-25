class Solution:
    def countDuplicates(self, n: int, m: int, h: List[int],
                        v: List[int]) -> int:

        hor = [1 for i in range(n)]
        ver = [1 for i in range(m)]

        for x in h:
            hor[x] = 0

        for x in v:
            ver[x] = 0

        temp_h = 1
        fin_h = 1
        for i in range(n):
            if hor[i]:
                temp_h = 1
            else:
                temp_h += 1
                fin_h = max(temp_h, fin_h)

        temp_v = 1
        fin_v = 1
        for i in range(n):
            if hor[i]:
                temp_v = 1
            else:
                temp_v += 1
                fin_v = max(temp_v, fin_v)

        return fin_h * fin_v
