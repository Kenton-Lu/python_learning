# LeetCode 1004. Max Consecutive Ones III
#
# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array
# if you can flip at most k 0's.
#
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
#
# Explanation:
# Flip two 0's to 1's, then the longest subarray of 1's is 6.
#
# Example 2:
# Input: nums = [0,0,1,1,1,0,0], k = 0
# Output: 3
#
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1
# 0 <= k <= nums.length



class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                zero_count +=1
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1

            ans = max(ans, right - left + 1)
            print(right,left,zero_count,ans)

        return ans


# 測試
nums = [1,0,1,0,1,0,1,1,1,1,0]
k = 2

print(Solution().longestOnes(nums, k))