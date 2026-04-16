# LeetCode 904. Fruit Into Baskets
#
# You are visiting a farm that has a single row of fruit trees.
#
# The trees are represented by an integer array fruits where fruits[i]
# is the type of fruit the i-th tree produces.
#
# You want to collect as much fruit as possible. However, the owner has
# some strict rules:
#
# - You only have two baskets.
# - Each basket can only hold a single type of fruit.
# - There is no limit on the amount of fruit each basket can hold.
# - Starting from any tree, you must pick exactly one fruit from every tree
#   while moving to the n.
# - Once you reach a tree with fruit that cannot fit in your baskets, you stop.
#
# Return the maximum number of fruits you can pick.
#
# Example 1:
# Input: fruits = [1,2,1
# Output: 3
#
# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
#
# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
#
# Constraints:
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length


from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        max_f = 0
        left = 0
        for right in range(len(fruits)):
            if fruits[right] not in seen:
                seen[fruits[right]] = 1
            else:
                seen[fruits[right]] += 1

            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1

            max_f = max(max_f, right - left + 1)
        return max_f
    
fruits = [1,2,3,2,2]

result = Solution().totalFruit(fruits)
print(result)