#Find 2 numbers that give desired sum in an array. T - O(n)  S - O(n) due to additional dictionary 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {} 
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in visited:
                return [ visited[remaining], i]
            else:
                visited[nums[i]] = i
        
