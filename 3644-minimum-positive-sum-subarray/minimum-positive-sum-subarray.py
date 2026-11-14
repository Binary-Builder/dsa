class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')  # Initialize minimum sum to infinity
      
        # Try all possible starting positions for subarrays
        for start in range(n):
            current_sum = 0
          
            # Extend the subarray from the starting position
            for end in range(start, n):
                current_sum += nums[end]
                subarray_length = end - start + 1
              
                # Check if subarray meets the conditions:
                # 1. Length is between l and r (inclusive)
                # 2. Sum is positive
                if l <= subarray_length <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
      
        # Return -1 if no valid subarray found, otherwise return minimum sum
        return -1 if min_sum == float('inf') else min_sum
