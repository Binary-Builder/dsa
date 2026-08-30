class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # Find indices of minimum and maximum elements
        min_index = 0
        max_index = 0
      
        # Iterate through array to find positions of min and max elements
        for i, num in enumerate(nums):
            if num < nums[min_index]:
                min_index = i
            if num > nums[max_index]:
                max_index = i
      
        # Ensure min_index is always less than or equal to max_index
        # This simplifies the calculation logic
        if min_index > max_index:
            min_index, max_index = max_index, min_index
      
        # Calculate minimum deletions using three strategies:
        # 1. Delete from left until both elements are removed (max_index + 1)
        # 2. Delete from right until both elements are removed (len(nums) - min_index)
        # 3. Delete from left to remove first element, then from right to remove second
        #    (min_index + 1) + (len(nums) - max_index)
        return min(
            max_index + 1,                              # Strategy 1: all from left
            len(nums) - min_index,                      # Strategy 2: all from right
            min_index + 1 + len(nums) - max_index       # Strategy 3: from both ends
        )
