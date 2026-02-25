# 304. Range Sum Query 2D - Immutable

**Difficulty:** Medium  
**Topic:** 2D Prefix Sum / Dynamic Programming  
**Link:** [LeetCode 304](https://leetcode.com/problems/range-sum-query-2d-immutable)

---

## Problem

Given a 2D matrix, handle multiple queries that calculate the **sum of elements** inside a rectangle defined by its upper left `(row1, col1)` and lower right `(row2, col2)` corners.

`sumRegion` must run in **O(1)** time.

---

## Approach — 2D Prefix Sum

Build a `sumMat` where each cell stores the cumulative sum of all elements above and to the left of it. This allows any rectangular region sum to be computed in constant time using inclusion-exclusion:
```
sumRegion = sumAtPos - sumAtLeft - sumAtTop + sumAtTopLeft
```

- **Preprocessing:** O(m × n)
- **Query:** O(1)
- **Space:** O(m × n)

---

## Solution
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for c in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        sumAtPos     = self.sumMat[r2][c2]
        sumAtLeft    = self.sumMat[r2][c1-1]
        sumAtTop     = self.sumMat[r1-1][c2]
        sumAtTopLeft = self.sumMat[r1-1][c1-1]

        return sumAtPos - sumAtLeft - sumAtTop + sumAtTopLeft
```

---

## Example

| Query | Result |
|---|---|
| sumRegion(2, 1, 4, 3) | 8 |
| sumRegion(1, 1, 2, 2) | 11 |
| sumRegion(1, 2, 2, 4) | 12 |