class Solution:
    def trap(self, height):
        if len(height) < 2:
            return 0
        left=[height[0]]
        for i in range(1,len(height)):
            if height[i]> left[-1]:
                left.append(height[i])
            else:
                left.append(left[i-1])
        right=[height[-1]]
        for i in range(len(height)-2, -1, -1):

            if height[i]> right[-1]:
                right.append(height[i])
            else:
                right.append(right[-1])
        right.reverse()
        result=0
        print(left,right)
        for i in range(len(height)):

            result+=min(left[i],right[i])-height[i]
        return result