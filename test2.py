from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1, nums2, and the end of nums1's actual size
        p1 = m - 1  # Last element in nums1's initial part
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last position in nums1

        # While there are elements to be compared in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:  # nums1[2 == 4] > nums2 [2 == 3] => nums1 [5 == 0] = nums1 [2 ==4]   #
                nums1[p] = nums1[p1]   # nums1 [5 == 0] = nums1 [2 ==4]
                p1 -= 1                # 2 - 1
            else:
                nums1[p] = nums2[p2]    #nums1[5 ] = nums2 [2 = 4] 
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them over
        # Note: No need to copy the remaining elements of nums1, since they are already in place
        while p2 >= 0:
            nums1[p] = nums2[p2]  ##nums1[5] = nums2 [2 = 4] 
            p2 -= 1
            p -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
