class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(char.lower() for char in s if char.isalnum())
        return s2 == s2[::-1]