class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
      
        # dp_closed[i][j] = number of ways to partition i points into j+1 segments
        # where the last segment is "closed" (doesn't extend to point i)
        dp_closed = [[0] * (k + 1) for _ in range(n + 1)]
      
        # dp_open[i][j] = number of ways to partition i points into j+1 segments  
        # where the last segment is "open" (extends to point i)
        dp_open = [[0] * (k + 1) for _ in range(n + 1)]
      
        # Base case: 1 point with 0 segments (1 way - the point itself)
        dp_closed[1][0] = 1
      
        # Fill the DP table for each number of points
        for num_points in range(2, n + 1):
            for num_segments in range(k + 1):
                # A closed segment at position i can come from:
                # 1. A closed segment at i-1 (we don't extend it)
                # 2. An open segment at i-1 (we close it here)
                dp_closed[num_points][num_segments] = (
                    dp_closed[num_points - 1][num_segments] + 
                    dp_open[num_points - 1][num_segments]
                ) % MOD
              
                # An open segment at position i extends from i-1
                dp_open[num_points][num_segments] = dp_open[num_points - 1][num_segments]
              
                if num_segments > 0:
                    # We can also start a new open segment at position i
                    # This requires one less segment to be already formed at i-1
                    dp_open[num_points][num_segments] = (
                        dp_open[num_points][num_segments] +
                        dp_closed[num_points - 1][num_segments - 1] +
                        dp_open[num_points - 1][num_segments - 1]
                    ) % MOD
      
        # Return the total number of ways (both closed and open final segments)
        return (dp_closed[n][k] + dp_open[n][k]) % MOD
