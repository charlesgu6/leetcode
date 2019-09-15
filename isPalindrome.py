class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ = str(x)
        x_ = list(x_)
        if x_[::-1] == x_:
            return True
        else:
            return False