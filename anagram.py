"""
Problem Statement: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        print(True if s == t else False)


new_sol = Solution()
new_sol.isAnagram("anagram", "nagaram")
