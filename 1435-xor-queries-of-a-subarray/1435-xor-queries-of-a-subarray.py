class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        length = len(bin(max(arr))[2:])
        def xor(a, b):
            new = ""
            for i,j in zip(a,b):
                new += str(int(i) ^ int(j))
            return new

        prefix = [bin(arr[0])[2:].zfill(length)]
        for i in range(1, len(arr)):
            prev = prefix[-1].zfill(length)
            curr = bin(arr[i])[2:].zfill(length)
            new = xor(prev, curr)
            prefix.append(new)
        
        # postfix = [bin(arr[-1])[2:]]
        # for i in range(len(arr) -2, -1, -1):
        #     prev = prefix[-1]
        #     curr = bin(arr[i])[2:]
        #     new = xor(prev, curr)
        #     postfix.append(new)
        #print(prefix)
        res = []
        for query in queries:
            i, j = query[0], query[1]
            if i == j:
                res.append(arr[i])
            else:
                if i > 0:
                    val = xor(prefix[j], prefix[i-1])
                    print(val)
                    res.append(int(val, 2))
                else:
                    res.append(int(prefix[j], 2))
        return res
