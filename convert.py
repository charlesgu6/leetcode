class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        row_num = 0
        flag = True#True 代表往下加；False 代表往上减
        for i in range(numRows):
            rows.append([])
        for i in range(len(s)):
            rows[row_num].append(s[i])
            if numRows -1 == 0:
                flag = True
            else:
                if row_num == 0:
                    flag = True
                if row_num == numRows - 1:
                    flag = False
                if flag == True:
                    row_num += 1
                else:
                    row_num -= 1
        res = [''.join(i) for i in rows]
        res = ''.join(res)
        return res

if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 1

    sovler = Solution()
    ans = sovler.convert(s,numRows)
    print(ans)

            
            