
# A program to find the largest k element in an array given that the integer has a negative value in the list
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       """
        largest_k = -1

        # convert the list to a set
        num_set = set(nums)
        # iterate ove the list
        for num in nums:
            # compare each element with the ones in the set to find whether it's negative exists
            if -num in num_set:
                largest_k = max(largest_k, abs(num))
        if largest_k > -1:
            return largest_k
        else:
            return -1


# create a list
nums = [-1, 10, 6, 7, -7, 1]

# create an instance of the solution class
sol = Solution()
# call the findmaxk function and pass the list
sol.findMaxK(nums)
