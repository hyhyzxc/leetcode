class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        d = set()

        for f in folder:
            f = f.split("/")[1:]
            currStr = ""

            isSub = False
            for sub in f:
                currStr += "/" + sub
                if currStr in d:
                    isSub = True
                    break
            if not isSub:
                d.add(currStr)
        return list(d)