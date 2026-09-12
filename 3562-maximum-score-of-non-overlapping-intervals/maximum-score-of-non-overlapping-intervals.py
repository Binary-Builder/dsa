from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store (l, r, weight, original_index)
        sorted_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            sorted_intervals.append((l, r, w, i))
            
        # Sort intervals primarily by start time l
        sorted_intervals.sort(key=lambda x: x[0])
        starts = [x[0] for x in sorted_intervals]
        
        # Precompute the next non-overlapping index for each interval
        next_idx = []
        for i in range(n):
            r = sorted_intervals[i][1]
            # Next interval must start strictly after current interval ends (l > r)
            idx = bisect_left(starts, r + 1)
            next_idx.append(idx)
            
        # dp[i][k] stores (max_weight, lexicographically_smallest_index_list)
        # for selecting at most k intervals from suffix starting at index i
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Fill DP table backwards (from n-1 down to 0)
        for i in range(n - 1, -1, -1):
            curr_w = sorted_intervals[i][2]
            curr_orig_idx = sorted_intervals[i][3]
            nxt = next_idx[i]
            
            for k in range(1, 5):
                # Option 1: Skip interval i
                best_w, best_path = dp[i + 1][k]
                
                # Option 2: Take interval i
                take_w, nxt_path = dp[nxt][k - 1]
                cand_w = curr_w + take_w
                
                # Form candidate indices list and keep it sorted
                cand_path = sorted(nxt_path + [curr_orig_idx])
                
                # Compare candidate option vs skipping option
                if cand_w > best_w:
                    best_w = cand_w
                    best_path = cand_path
                elif cand_w == best_w:
                    # Lexicographical tie-breaker
                    if best_path == [] or cand_path < best_path:
                        best_path = cand_path
                
                dp[i][4 - (4 - k)] = (best_w, best_path)

        return dp[0][4][1]