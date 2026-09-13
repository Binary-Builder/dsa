class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)

        translation_count = Counter()

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    for h in range(n):
                        for k in range(n):
                            if img2[h][k] == 1:
                                trans_vector = (i - h, j - k)

                                translation_count[trans_vector] += 1
        return max(translation_count.values()) if translation_count else 0