from collections import defaultdict
from math import sqrt
class Solution:
    def maximumDetonation(self, bombs) -> int:
        self.graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                diff =  sqrt((bombs[j][0] - bombs[i][0])**2 + (bombs[j][1] - bombs[i][1])**2)
                if diff <= bombs[i][2]:
                    self.graph[i].append(j)
        res = 0
        for i in range(len(bombs)):
            self.visited = set([i])
            self.dfs(i)
            res = max(res,len(self.visited))
        return res
    def dfs(self,node):
        for child in self.graph[node]:
            if child not in self.visited:
                self.visited.add(child)
                self.dfs(child)
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
    

