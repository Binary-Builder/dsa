from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Determine if two rectangles overlap.
      
        Args:
            rec1: First rectangle represented as [x1, y1, x2, y2] where 
                  (x1, y1) is bottom-left corner and (x2, y2) is top-right corner
            rec2: Second rectangle represented as [x3, y3, x4, y4] where
                  (x3, y3) is bottom-left corner and (x4, y4) is top-right corner
      
        Returns:
            True if rectangles overlap, False otherwise
        """
        # Extract coordinates for first rectangle
        x1, y1, x2, y2 = rec1
      
        # Extract coordinates for second rectangle  
        x3, y3, x4, y4 = rec2
      
        # Check if rectangles do NOT overlap:
        # - rec2 is completely above rec1 (y3 >= y2)
        # - rec2 is completely below rec1 (y4 <= y1)
        # - rec2 is completely to the right of rec1 (x3 >= x2)
        # - rec2 is completely to the left of rec1 (x4 <= x1)
        # If none of these conditions are true, rectangles must overlap
        return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)
