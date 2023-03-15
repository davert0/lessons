class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table = [[None] * (len(s)) for _ in range(numRows)]
        should_write_diagonal = False
        i = 0
        j = 0
        res = ""
        if numRows == 1:
            return s
        if numRows == 2:
            a = [s[i] for i in range(len(s)) if i % 2 == 0]
            b = [s[i] for i in range(len(s)) if i % 2 != 0]
            for row in [a, b]:
                res += "".join(row)
            return res

        for l in s:

            if i < numRows and not should_write_diagonal:
                table[i][j] = l
                i += 1
            elif not should_write_diagonal:
                should_write_diagonal = True
                i -= 1

            if should_write_diagonal:
                i -= 1
                j += 1
                table[i][j] = l
                if i == 1:
                    i = 0
                    j += 1
                    should_write_diagonal = False

        for i in table:
            for j in i:
                if isinstance(j, str):
                    res += j

        return res
            
s = Solution()
print(s.convert("ABCDEF", 2))