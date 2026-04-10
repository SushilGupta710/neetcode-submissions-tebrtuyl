class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #here we will not sort because we need to work with index

        maxContArea=0
        l,r=0,len(heights)-1
        while l<r:
            # get the min height of container
            h=min(heights[l],heights[r])
            #get the width of container
            w=r-l #small to big number
            #now get the area
            area=h*w #height x width
            #We got the area now let's get the maxarea among area and maxarea
            maxContArea = max(maxContArea,area)
            #now this is common step if l value is small then r value then increase r count by 1
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxContArea        