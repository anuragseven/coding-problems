class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp=nums1[0:m]
        i=0
        j=0
        temp.append(float('inf'))
        nums2.append(float('inf'))
        for k in range(0,m+n):
            if temp[i]<=nums2[j]:
                nums1[k]=temp[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1