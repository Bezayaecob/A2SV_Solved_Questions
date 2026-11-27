class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            if s[i].isupper():
                res+=s[i].lower()
            else:
                res+=s[i]
        return res