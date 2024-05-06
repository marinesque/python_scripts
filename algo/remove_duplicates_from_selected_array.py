"""

26

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

"""
from typing import List


class Solution:
    @classmethod
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1

    @classmethod
    def removeDuplicates2(nums: List[int]) -> int:
        # Initialize the current position index.
        cur = 0
        # Initialize the variable to keep track of the last unique number processed.
        last = None
        # Iterate over each number in the input list.
        for n in nums:
            # If the current number is the same as the last unique number, skip it.
            if n == last: continue
            # Update the last unique number processed.
            last = n
            # Replace the element at the current position with the new unique number.
            nums[cur] = n
            # Move to the next position.
            cur += 1
        # Return the new length of the array after removing duplicates.
        return cur

"""
# This block ensures that the following code runs only when the script is executed directly, not when imported.
if __name__ == '__main__':
    # Import necessary modules for reading input and writing output.
    import json, sys
    # Open a file named 'user.out' for writing.
    with open('user.out', 'w') as f:
        # Read JSON-encoded data from stdin and convert it to Python objects.
        data = map(json.loads, sys.stdin)
        # Iterate over each list of numbers in the input data.
        for nums in data:
            # Call the main function with the current list to remove duplicates.
            k = Solution.removeDuplicates2(nums)
            # Write the modified list (up to the new length `k`) to the file in JSON format.
            print(json.dumps(nums[:k], separators=(',',':')), file=f)
    # Exit the script.
    sys.exit()
"""

list = [1, 2, 2, 3, 4, 4]
k = Solution.removeDuplicates(list)
print(k)
