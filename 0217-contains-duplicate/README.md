# 217. Contains Duplicate

**Difficulty:** Easy  
**Topic:** Arrays / Hash Set  
**Link:** [LeetCode 217](https://leetcode.com/problems/contains-duplicate)

---

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice**, and `false` if every element is distinct.

---

## Approach — Hash Set

Iterate through the array and track seen elements using a set. If a number is already in the set, return `true` immediately. Otherwise add it and continue.

- **Time:** O(n)
- **Space:** O(n)

---

## Solution
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

## Examples

| Input | Output |
|---|---|
| [1, 2, 3, 1] | true |
| [1, 2, 3, 4] | false |
| [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] | true |