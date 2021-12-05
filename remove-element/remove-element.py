class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        if nums[l] == val:
            return l
        return l + 1