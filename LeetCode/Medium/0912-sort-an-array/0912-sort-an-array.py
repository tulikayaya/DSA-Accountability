class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        def merge(arr, L, M, R):
            left_arr, right_arr = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0 #rewrite in arr, j = pointer for left_arr, k = pointer for R

            while j < len(left_arr) and k < len(right_arr):
                if left_arr[j] <= right_arr[k]:
                    arr[i] = left_arr[j]
                    j+=1
                else:
                    arr[i] = right_arr[k]
                    k += 1
                i += 1
            
            while j < len(left_arr):
                arr[i] = left_arr[j]
                i+= 1
                j+=1
            
            while k < len(right_arr):
                arr[i] = right_arr[k]
                k+= 1
                i += 1
            return arr

        def mergeSort(arr, left, right):
            if left == right:
                return

            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid +1, right)
            merge(arr, left, mid, right)
            return arr
        
        return mergeSort(nums, 0, len(nums)-1)