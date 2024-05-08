# Brute-force approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

# Two-pass hash-map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersMap = {}

        # Building hash-map with numbers from list
        for i in range(len(nums)):
            numbersMap[nums[i]] = i

        # Find the complement
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numbersMap and numbersMap[complement] != i:
                return [i, numbersMap[complement]]

        return []

# One-pass hash-map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numbersMap:
                return [numbersMap[complement], i]

            numbersMap[nums[i]] = i

        return []
