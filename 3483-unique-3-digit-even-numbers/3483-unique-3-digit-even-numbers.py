class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums= set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or i==k or j==k:
                        continue
                    a=digits[i]
                    b=digits[j]
                    c=digits[k]
                    if a==0:
                        continue
                    if c % 2 !=0:
                        continue
                    num= a*100 + b*10 + c
                    nums.add(num)
        return len(nums)