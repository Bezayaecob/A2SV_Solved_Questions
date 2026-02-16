class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      if len(word1) != len(word2): 
        return False
      c_word1= Counter(word1)
      c_word2= Counter(word2) 
      return (c_word1.keys()==c_word2.keys()) and (sorted(c_word1.values())==sorted(c_word2.values()))
