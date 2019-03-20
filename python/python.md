- [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)

```
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        
        left = [max(grid[i]) for i in range(x)]
        top = [max([grid[j][i] for j in range(x)]) for i in range(y)]
        
        res = 0
        for i in range(x):
            for j in range(y):
                tmp_max = min(left[i], top[j])
                res += tmp_max - grid[i][j]
        return res
```

