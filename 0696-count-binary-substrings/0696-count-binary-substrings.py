class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        previous = 0
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += min(count, previous)
                previous = count
                count = 1

        result += min(count, previous)

        return result