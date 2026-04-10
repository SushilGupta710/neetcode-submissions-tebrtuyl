class Solution:
    def trap(self, height: List[int]) -> int:
        #Return 0 simply if there is no height value
        if not height:
            return 0 
        #declare variables
        result=0
        length=len(height)
        l,r=0,length-1
        #define maxLeft and maxRight Height with default respective value
        maxLeft=height[l]
        maxRight=height[r]

        #run while loop because we want result in 0(1) as two pointer
        #we always know l index will alwas be shorter and till them we have to run
        while l<r:
            #check first maxL and maxR are alse less the increase the l count
            if maxLeft < maxRight:
                l+=1 #increase l count simply
                #assign the max value in left with current value
                maxLeft=max(maxLeft,height[l])
                #Now add the result whith currecnt value check with max value
                result+=maxLeft - height[l]
            else:
                r-=1
                maxRight=max(maxRight,height[r])
                result +=maxRight - height[r]
        return result



