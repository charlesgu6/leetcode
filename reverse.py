class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            flag = False
        else:
            flag = True
        x = [x[i] for i in range(len(x))]
        x = x[::-1]
        x = ''.join(x)
        x = int(x)
        if x < (-2 ** 31) or x > (2 ** 31 -1):
            x = 0
        if flag == False:
            x = -x
        return x

if __name__ == "__main__":
    x = -123

    sovler = Solution()
    ans = sovler.reverse(x)
    print(ans)
