class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = []
        stack = []
        map = {}
        #nums2 = [1,3,4,2]

        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                    ele = stack.pop()
                    map[ele] = nums2[i] 

            stack.append(nums2[i])
        
        for i,n in enumerate(nums1):
            if n not in map:
                ans.append(-1)
            else:
                ans.append(map[n])

        return ans
