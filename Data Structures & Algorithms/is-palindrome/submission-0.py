class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s.lower()))

        start = 0
        end = len(clean) - 1

        for char in range(len(clean)):
            if start < end:
                if clean[start] != clean[end]:
                    return False
                start += 1
                end -= 1
            else:
                break

        return True