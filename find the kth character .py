class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            new = ""
            for c in word:
                new += chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
            word += new
        return word[k-1]
