class Solution:
    def jump(self, nums: List[int]) -> int:
        
        [2,3,1,1,4]
        dp = {}
        def calcJumps(i):
            if i == len(nums) - 1: return 0
            if i in dp: return dp[i]
            maxLength = nums[i]
            minJumps = len(nums)
            for x in range(1, maxLength + 1):
                if i + x < len(nums):
                    minJumps = min(minJumps, calcJumps(i+x))
            dp[i] = 1 + minJumps
            return 1 + minJumps
        return calcJumps(0)