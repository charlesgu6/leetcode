class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        if str[0].isdigit() or str[0] == '-' or str[0] == '+':
            res = []
            flag = True
            for i in range(len(str)):
                if i == 0:
                    if str[i] == '-':
                        flag = False
                    elif str[i] == '+':
                        flag = True
                    elif str[i].isdigit():
                        res.append(str[i])
                elif str[i].isdigit():
                    res.append(str[i])
                else:
                    break
            res = ''.join(res)
            if len(res) ==0:
                return 0
            res = int(res)
            if flag == False:
                res = -res
            if res < (-2 ** 31):
                res = (-2 ** 31)
            if res > (2 ** 31 -1):
                res = (2 ** 31 -1)
            return res

        else:
            return 0

if __name__ == "__main__":
    x = "+"
    sovler = Solution()
    ans = sovler.myAtoi(x)
    print(ans)