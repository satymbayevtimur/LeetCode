# First approach

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
                
        return j

# Second approach

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
		slow, fast = 0, 1
        
		while fast in range(len(nums)):
			if nums[slow] == nums[fast]:
				fast += 1
			else:
				nums[slow+1] = nums[fast]
				fast += 1
				slow += 1

		return slow + 1

# Third approach

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

	    while i < len(nums):
			if nums[i] == nums[i - 1]:
				nums.pop(i)
			else:
				i += 1

		return len(nums)

# Fourth approach

from collections import OrderedDict

class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] =  OrderedDict.fromkeys(nums)
        return len(nums)
