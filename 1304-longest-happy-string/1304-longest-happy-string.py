class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        nums = [('a', a), ('b', b), ('c', c)]
        nums.sort(key = lambda x: x[1])

        res = ""

        while True:
            letter, most_common = nums[-1]
            #print(nums)
            if most_common <= 0:
                return res
            
            if len(res) >= 2 and res[-1] == res[-2] and res[-1] == letter:
                letter, most_common = nums[-2]
                if most_common <= 0:
                    letter, most_common = nums[0]
                
                if most_common <= 0:
                    return res
            
            res += letter
            nums.remove((letter, most_common))
            nums.append((letter, most_common - 1))
            nums.sort(key = lambda x: x[1])