"""
PROBLEM sTATEMENT:
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A variable to hold the maximum product
        max_prod = int()
        # create a loop to iterate over each element
        for i in range(len(nums)):
            # second loop to multiply each element in the first loop
            for j in range(i+1, len(nums)):
                product = (nums[i] - 1)*(nums[j] - 1)
                max_prod = max(max_prod, product)
        return max_prod


# create the list
nums = [1, 5, 4, 5]
max_product = Solution()
max_product.maxProduct(nums)
