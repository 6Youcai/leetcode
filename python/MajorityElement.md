# 回字的四种写法

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 n/2 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

## Brute Force
暴力枚举数组中的每个元素，统计其出现次数，如果超过半数就返回；
```
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
```

## HashMap
使用哈希映射来存储每个元素以及出现的次数，返回值最大的键；
```
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

## Sorting
先将数组排序，然后返回数组中间的元素；
既然超过一半，无论怎么摆放排序后的元素，中间位置都会被众数占据；
![](https://leetcode.com/problems/majority-element/Figures/169/sorting.png)
```
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
```

## Randomization
随缘吧，反正选到正确答案的概率还蛮大的。
```
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
```

## Divide and Conquer
拆分后我依然是老大，而且比另一半的老大还要大。
```
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
```

## Boyer-Moore Voting Algorithm
依次上擂台拉一个反对派下来，没有反对派就留下；
```
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
[叹为观止](https://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html)
