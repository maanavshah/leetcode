class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return chars
        count = 1
        s = []
        prev = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                s.append(prev)
                if count > 1:
                    s.append(str(count))
                    count = 1
                prev = chars[i]
            if i == len(chars) - 1:
                s.append(prev)
                if count > 1:
                    s.append(str(count))
        return len(s)
