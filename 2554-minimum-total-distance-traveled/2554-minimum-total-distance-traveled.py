class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda x: x[0])
        factory_pos = [f[0] for f in factory]
        capacities = [f[1] for f in factory]
        dp = {}
        def dfs(currRobot, currFactory, usedCapacity):
            if currRobot == len(robot):
                return 0
            if currFactory == len(factory):
                return float("inf")
            key = (currRobot, currFactory, usedCapacity)
            if key in dp:
                return dp[key]
            minDist = dfs(currRobot, currFactory+1, 0)

            capacity = capacities[currFactory]
            if usedCapacity < capacity:
                minDist = min(minDist, dfs(currRobot+1, currFactory, usedCapacity+1) + abs(robot[currRobot] - factory_pos[currFactory]))
            
            dp[key] = minDist
            return minDist
        return dfs(0,0,0)
            
