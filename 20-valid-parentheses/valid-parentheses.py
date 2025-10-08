class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i in "[({":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if (top == "(" and i == ")") or (top == "[" and i == "]") or (top == "{" and i == "}"):
                    stack.pop()
                else:
                    return False
        return not stack