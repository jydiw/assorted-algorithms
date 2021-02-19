'''
Given a sorted array nums, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2 -- since nums = [1,2]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5 -- since nums = [0,1,2,3,4]

Constraints:
0 <= nums.length <= 3 * 104
-10**4 <= nums[i] <= 10**4
nums is sorted in ascending order.
'''

def removeDuplicates(nums):
    a = 0
    for b in range(1, len(nums)):
        if nums[a] != nums[b]:
            a += 1
            nums[a] = nums[b]
    return a + 1

test_cases = [
  [1,1,2],
  [0,0,1,1,1,2,2,3,3,4]
]

removeDuplicates(test_cases[1])