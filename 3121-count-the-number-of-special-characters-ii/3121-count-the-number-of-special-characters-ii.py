class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = {}
        lower = {}

        for i in range(len(word)):
            letter = word[i]

            if letter.isupper():
                if letter not in upper:
                    upper[letter] = i
            else:
                lower[letter] = i

        count = 0

        for letter in lower:
            capital = letter.upper()

            if capital in upper:
                if lower[letter] < upper[capital]:
                    count += 1

        return count
        