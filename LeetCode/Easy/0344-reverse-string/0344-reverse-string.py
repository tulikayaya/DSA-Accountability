class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1

        while left <= right:
            copy = s[right]
            s[right] = s[left]
            s[left] = copy
            left += 1
            right -= 1 