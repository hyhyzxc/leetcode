class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_list = [bin(c)[2:].zfill(24) for c in candidates]
        counts = [0] * 24
        #print(bit_list)
        for i in range(24):
            count = 0
            for bit in bit_list:
                if bit[i] == "1":
                    count += 1
            counts[i] = count
        return max(counts)