class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def get_area(l:int, r:int, heights: List[int]) -> int:
            return (r-l)*min(heights[l], heights[r])

        l = 0
        r = len(heights)-1
        M = 0

        while l<r:
            area = get_area(l,r,heights) 
            if area < M:
                pass

            else:
                M = area

            if heights[l] < heights[r]:
                l += 1

            else:
                r -=1
        
        return M