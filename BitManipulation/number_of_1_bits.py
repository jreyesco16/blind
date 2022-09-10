class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bit_str = '{0:08b}'.format(n)
        
        bit_str = bit_str.replace("0", "")
        
        return len(bit_str)