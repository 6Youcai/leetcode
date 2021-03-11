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

- [Power of Three](https://leetcode.com/problems/power-of-three/)

```
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3**0 = 1
        if n < 1:
            return False
        while n % 3 == 0:
            n = n / 3
        if n == 1:
            return True
        return False
```

计算一个数是否为3的幂次方，一种方法是从小到大计算3^1 3^2 3^n，直至结果大于等于输入的数；另一种思路是看这个数是否为3的倍数；以输入100为例，第一种法法需要计算直至3^5，而后一种方法则只需进行一次计算，提高了效率。

- [Keyboard Row](https://leetcode.com/problems/keyboard-row/)

```
import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [w for w in words if re.search("^([asdfghjkl]+|[zxcvbnm]+|[qwertyuiop]+)$", w, re.I)]
```

一开始使用的办法不够优雅，直至看到[这个答案](https://leetcode.com/problems/keyboard-row/discuss/259735/Python-one-liner-with-regex)。

- [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

判断两个数的和是否能够被一个数整除，最简单的想法是将所有的组合计算一下，然而当我这么做了，却得到`Time Limit Exceeded`，翻看讨论看到[这位老兄的方法](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60)，简直是帅呆了。

不就是两个数嘛，一个数能提供一部分，另外看还有几个数能满足另一部分，并将中间的一些过程记录下来。

```
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainder = {}
        res = 0
        for t in time:
            # this t need one be paird
            ne = -t % 60
            res += remainder.get(ne, 0)

            # this t produce
            re = t % 60
            remainder[re] = remainder.get(re, 0) + 1

        return res
```

- [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

```
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 因为饥饿度最小的孩子最容易吃饱，所以我们先考虑这个孩子
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            child += 1 if g[child] <= s[cookie] else 0
            cookie += 1
        return  child
```

- [Candy](https://leetcode.com/problems/candy/)

```
class Solution:
    def candy(self, ratings: List[int]) -> int:
        L = len(ratings)
        if L == 1:
            return 1

        out = [1] * L # 初始化
        # 如果右边孩子的评分比左边的高
        for i in range(L-1):
            if ratings[i] < ratings[i+1]:
                out[i+1] = out[i] + 1
        # 如果左边孩子的评分比右边的高
        for i in range(L-1, 0, -1):
            if ratings[i-1] > ratings[i] and out[i-1] <= out[i]:
                out[i-1] = out[i] + 1
        return sum(out)
```

```{c++}
class Solution {
public:
    int candy(vector<int>& ratings) {
        int L = ratings.size();
        if(L==1)
            return 1;
        vector<int> res(L, 1);
        for(int i=0; i<L-1; i++) {
            if(ratings[i] < ratings[i+1])
                res[i+1] = res[i] +1;
        }
        for(int i=L-1; i>0; i--) {
            if(ratings[i-1] > ratings[i] && res[i-1] <= res[i])
                res[i-1] = res[i] + 1;
        }         
        return accumulate(res.begin(), res.end(), 0);
    }
};
```

- [Prime Palindrome](https://leetcode.com/problems/prime-palindrome/)

```
def isPrime(N):
    m = int(math.sqrt(N))
    for i in range(2, N**0.5 + 1):
        if N%i == 0:
            return False
    return True

class Solution:
    # my own code
    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2
        while True:
            s = str(N)
            if s == s[::-1]:
                if isPrime(N):
                    return N
            # the next Palindrme, core
            l = len(s)
            if l < 2:
                N += 1
                continue
            if s == '9' * l:
                N += 2
                continue
            left = s[: l//2]
            if l%2 == 0:
                p = int(left + left[::-1])
                if N < p:
                    N = p
                else:
                    left = str(int(left) + 1)
                    N = int(left + left[::-1])
                continue
            else:
                mid = s[l//2]
                p = int(left + mid + left[::-1])
                if N < p:
                    N = p
                else:
                    if mid != '9':
                        mid = str(int(mid) + 1)
                        N = int(left + mid + left[::-1])
                    else:
                        left = str(int(left)+1)
                        N = int(left + '0' + left[::-1])
                continue
```
