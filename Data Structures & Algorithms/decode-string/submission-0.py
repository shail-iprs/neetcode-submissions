class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        curr_str=""
        curr_num=0

        for item in s:
            if item.isdigit():
                curr_num=curr_num*10+int(item)
            elif item.isalpha():
                curr_str=curr_str+item
            elif item=='[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str=""
                curr_num=0
            else:
                prev_num=stack.pop()
                prev_str=stack.pop()
                curr_str=prev_str+curr_str*prev_num
        return curr_str
