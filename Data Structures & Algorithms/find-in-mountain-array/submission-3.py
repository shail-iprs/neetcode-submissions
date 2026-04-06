class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak=-1

        left=1
        right=mountainArr.length()-2

        while left<=right:
            mid=left+(right-left)//2

            l,m,r=mountainArr.get(mid-1),mountainArr.get(mid),mountainArr.get(mid+1)
            if l>m>r:
                right=mid-1
            elif l<m<r:
                left=mid+1
            else:
                break
        peak=mid

        left=0
        right=peak-1

        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)<target:
                left=mid+1
            else:
                right=mid-1
        
        left=peak
        right=mountainArr.length()-1

        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                left=mid+1
            else:
                right=mid-1
        return -1

        