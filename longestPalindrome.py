class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        num_list = []
        num_max = [0,0]
        for i in range(len(s)):
            if i == 0:
                continue
            if i == 1:
                if s[i] == s[i-1]:
                    max_len = 2
                    num_max = [0,1]
                    num_list.append(0)
                continue

            del_num = []
            for j, begin in enumerate(num_list):
                if begin - 1 >= 0:
                    if s[i] == s[begin-1]:
                        num_list[j] -= 1
                    else:
                        if (i - begin) > max_len:
                            max_len = i - begin
                            num_max = [begin, i-1]
                        del_num.append(j)
                else:
                    if (i - begin) > max_len:
                        max_len = i - begin
                        num_max = [begin, i-1]
                    del_num.append(j)
            del_num.sort()
            for j in del_num[::-1]:
                del num_list[j]

            if s[i] == s[i-1]:
                num_list.append(i-1)
                if max_len < 2:
                    max_len = 2
                    num_max = [i-1,i]

            if s[i] == s[i-2]:
                num_list.append(i-2)
                if max_len < 3:
                    max_len = 3
                    num_max = [i-2, i]

        for i in num_list:
            if len(s) - i > max_len:
                max_len = len(s) - i
                num_max = [i, len(s)-1]

        return s[num_max[0]:num_max[1]+1]
                


if __name__ == "__main__":
    x = "eeeeeeeee"
    sovler = Solution()
    ans = sovler.longestPalindrome(x)
    print(ans)
#%%

#%%
5%2

#%%
