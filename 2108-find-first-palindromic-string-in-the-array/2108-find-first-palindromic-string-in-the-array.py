class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in range(len(words)):
            word= words[i]
            left=0
            right=len(word)-1
            isPalindrome=True
            while left < right:
                if word[left]!=word[right]:
                    isPalindrome=False
                    break 
                left+=1
                right-=1
            if isPalindrome:
                return word
        return ""

        