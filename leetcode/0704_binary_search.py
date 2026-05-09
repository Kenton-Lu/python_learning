class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


# Sample Test
nums = [-1,0,3,5,9,12]
target = 9

print(Solution().search(nums, target))


# Sample Test 2
nums = [-1,0,3,5,9,12]
target = 2

print(Solution().search(nums, target))