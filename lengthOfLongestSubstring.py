# %%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = []
        max_size = 0
        for i in range(len(s)):
            a = s[i]
            if s[i] in dic:
                dic = dic[dic.index(s[i])+1:]
            dic.append(s[i])
            size = len(dic)
            if size > max_size:
                max_size = size
        return max_size

if __name__ == "__main__":
    a = "aabaab!bb"

    solver = Solution()
    print(solver.lengthOfLongestSubstring(a))


#%%
