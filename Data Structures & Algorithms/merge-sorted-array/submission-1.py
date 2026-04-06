class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:


        #m=len(nums1)-1
        #n=len(nums2)-1
        i=m-1
        j=n-1
        k=m+n-1

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                #nums[k],nums[i]=nums[i],nums[k]
                nums1[k]=nums1[i]
                #k-=1
                i-=1
            else:
                #nums[k],nums[j]=nums[j],nums[k]
                nums1[k]=nums2[j]
                #k-=1
                j-=1
            k-=1
        return nums1

        