# 32 ms	14.4 MB
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        way = []
        x = 0
        y = 0
        way.append([x,y])
        for s in path:
            if s == 'N':
                x -= 1
            if s == 'E':
                y += 1
            if s == 'S':
                x += 1
            if s == 'W':
                y -= 1
            if [x,y] in way:
                return True
            else:
                way.append([x,y])
        return False