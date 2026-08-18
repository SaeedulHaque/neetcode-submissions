class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        check = {}
        for i in range(n):
            difference = target - nums[i]
            if difference in check:
                return [check[difference], i]
            else:
                check[nums[i]]=i