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

- [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)

```
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            local, domain = e.split('@')
            
            local = local.replace(".", "")
            local = local.split("+")[0]
            
            e = local + domain
            res.add(e)
            
        return len(res)
```

- [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)

```
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.",
                    "....","..",".---","-.-",".-..","--","-.",
                    "---",".--.","--.-",  ".-.","...","-",
                    "..-","...-",".--",   "-..-","-.--","--.."]
        res = set()
        for w in words:
            Morse = ""
            for c in w:
                Morse += alphabet[ord(c) - ord('a')]
            res.add(Morse)
        return len(res)
```

- [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

```
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        capture = []
        for c in A:
            if c in capture:
                return c
            else:
                capture.append(c)
```

- [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)

```
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False
        if moves.count('U') != moves.count('D'):
            return False
        if moves.count('L') != moves.count('R'):
            return False
        return True
```
