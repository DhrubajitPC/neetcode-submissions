class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # print(nums, target)
        while l <= r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:  # left half is sorted
                if nums[l] <= target and target <= nums[mid]:  # target in this half
                    r = mid - 1
                else:  # target in other half
                    l = mid + 1

            else:  # right half is sorted
                if nums[mid] <= target and target <= nums[r]:  # target in this half
                    l = mid + 1
                else:  # target in other half
                    r = mid - 1

        return -1