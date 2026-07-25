class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False