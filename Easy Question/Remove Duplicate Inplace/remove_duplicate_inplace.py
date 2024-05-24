"""
Remove the input value from the list.

"""

class Solution:
    def removeElement(self, nums, val: int) -> int:
        """
        :param nums: the list of integer
        :param val: value needed to be remove
        :return: k: the numbers of n_th first element in the list after remove is the result
        for example k = 5, nums = [2,3,5,2,7,2,4,7] -> actual result is [2,3,5,2,7]
        """
        k = 0
        for value in nums:
            if value != val:
                nums[k] = value
                k += 1
        return k, nums


solve = Solution()
print(solve.removeElement([2,3,4,4,5,2,4,7], 4))


