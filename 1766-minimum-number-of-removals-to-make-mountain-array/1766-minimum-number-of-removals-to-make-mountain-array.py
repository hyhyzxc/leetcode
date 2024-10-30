class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = [0 for i in range(len(nums))]
        lis[0] = 1

        for i in range(1,len(nums)):
            curr = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    curr = max(curr, lis[j])
            lis[i] = curr + 1
        
        lds = [0 for i in range(len(nums))]
        lds[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            curr = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[i]:
                    curr = max(curr, lds[j])
            lds[i] = curr + 1
        
        res = float('inf')

        for i, a in enumerate(lis):
            if i == 0 or i == len(nums) - 1 or a == 1:
                continue
            b = lds[i]
            if b == 1:
                continue
            res = min(len(nums) - a - b + 1, res)
        #     print(len(nums)-a-b+1)
        # print(lis)
        # print(lds)
        return res