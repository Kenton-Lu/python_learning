# LeetCode 239. Sliding Window Maximum
#
# You are given an array of integers nums, and there is a sliding window
# of size k which is moving from the very left of the array to the very right.
#
# You can only see the k numbers in the window. Each time the sliding window
# moves right by one position.
#
# Return the max sliding window.
#
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
#
# Explanation:
# Window position                Max
# ---------------------------    -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # 存 index，不是存 value
        res = []

        for right in range(len(nums)):

            # 1. 移除已經不在 window 裡的 index
            if dq and dq[0] <= right - k:
                print('1111111111')
                dq.popleft()

            # 2. 維持 deque 對應的值是由大到小
            # 如果新進來的 nums[right] 比尾巴大，尾巴就沒用了
            while dq and nums[dq[-1]] < nums[right]:
                print('2222222222')
                dq.pop()

            # 3. 把目前 index 放進 deque
            dq.append(right)

            # 4. 當 window 長度達到 k，開始記錄答案
            if right >= k - 1:
                print('444444444')
                res.append(nums[dq[0]])
            print('right',right,dq)

        return res
    

# 測試用
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Solution().maxSlidingWindow(nums, k))