#https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l=nums1+nums2
        l.sort()
        if len(l)==1:
            return l[0]/1
        elif len(l)%2==0:
            a=(l[(len(l)//2)-1]+l[len(l)//2])/2
            return a
        else:
            a=l[(len(l))//2]
            return a