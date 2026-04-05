class Solution:
    def reverseBits(self, n: int) -> int:
        bits= bin(n)[2:]
        bits=bits.zfill(32)
        reversed_bits=bits[::-1]
        return int(reversed_bits,2)

        