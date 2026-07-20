class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brk = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in brk:
                if stk and stk[-1] == brk[char]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)

        return True if not stk else False