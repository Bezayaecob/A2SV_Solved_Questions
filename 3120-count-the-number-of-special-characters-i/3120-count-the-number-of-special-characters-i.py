class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=set()
        count= 0
        for letter in word:
            if letter.lower() in word and letter.upper() in word:
                res.add(letter.lower())
       
        return len(res)