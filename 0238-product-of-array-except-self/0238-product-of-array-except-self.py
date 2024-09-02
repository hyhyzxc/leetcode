class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        s = 1
        for num in nums:
            s *= num
            prefix.append(s)
        
        postfix = []
        s = 1
        for num in nums[::-1]:
            s *= num
            postfix.append(s)
        #print(prefix, postfix)
        res = []
        for i in range(len(nums)):
            numLeft = i
            numRight = len(nums) - 1 - i
            pre = 1
            post = 1

            if numLeft > 0:
                pre = prefix[numLeft-1]
            if numRight > 0:
                post = postfix[numRight-1]
            res.append(pre * post)
        return res