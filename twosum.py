class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums:
                j = nums.index(num2)
                if i != j:
                     return [i,j]

if __name__ == "__main__":
     nums = [3,2,4]
     target = 6
     solver = Solution()
     answer = solver.twoSum(nums,target)
     print(answer)
