class point(object):
    def __init__(self,x,y,cnt) -> None:
        self.x = x
        self.y = y
        self.cnt = cnt

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        bfs_queue = []
        dx = [1, 1, 1, -1, -1, -1, 0, 0]
        dy = [1, 0, -1, 1, -1, 0, 1, -1]
        if len(grid) == 0:
            return -1
        if grid[0][0] == 1: return -1
        bfs_queue.append(point(0,0,1))
        grid[0][0] = -1
        row = len(grid)
        col = len(grid[0])
        while bfs_queue:
            cur = bfs_queue.pop(0)
            if (cur.x == row-1 and cur.y == col-1):
                return cur.cnt
            
            for i in range(0,len(dx)):
                x = cur.x + dx[i]
                y = cur.y + dy[i]
                if (x >= 0 and y >= 0 and x < row and y < col and grid[x][y] == 0):
                    bfs_queue.append(point(x,y,cur.cnt+1))
                    grid[x][y] = -1
            
        return -1
            

            




if __name__ == "__main__":
    obj = Solution()
    print(obj.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))