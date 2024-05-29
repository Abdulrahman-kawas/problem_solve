from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length1 = len(nums)
        for i in range(length1 - 1):  # Loop until the second to last element
            for j in range(i + 1, length1):  # Start from the next element
                if nums[i] + nums[j] == target:
                    return [i, j]
        print("No two sum solution")

sol = Solution()

# Example usage:
sol1 = sol.twoSum([2, 7, 11, 15], 9)
print(sol1)  # Output: [0, 1]
