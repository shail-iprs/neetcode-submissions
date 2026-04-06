class Solution:
    def lengthOfLongestSubstring(self, s):
        seen=set()
        res_str=''
        max_len=0
        left=0
        right=0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            res_str=s[left:right+1]
            max_len=max(max_len,right-left+1)
            right+=1
        print(res_str)
        return max_len