class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}

        stack = []

        for ss in s:
            if ss in brackets:
                # 如果是左，入栈
                stack.append(ss)

            else:
                # 如果是右，出栈并匹配
                
                # 如果stack 为空，出问题
                if not stack: return False

                if brackets[stack.pop()] != ss: return False

        if len(stack) != 0: return False

        return True
