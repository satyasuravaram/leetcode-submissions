class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        s = set()
        ans = 0
        total = 0
        while end < len(nums):
            if nums[end] in s:
                ans = max(ans, total)
                total += nums[end]
                for i in range(start, end):
                    total -= nums[i]
                    if nums[i] in s:
                        s.remove(nums[i])
                    if nums[i] == nums[end]:
                        start = i + 1
                        break
                s.add(nums[end])
            else:
                s.add(nums[end])
                total += nums[end]
                ans = max(ans, total)
            end += 1
            # print(start, end, total)

        return ans
        