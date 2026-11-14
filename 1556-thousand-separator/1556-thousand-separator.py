
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)

        if len(s) <= 3:
            return s
        elif len(s) <= 6:
            return s[:-3] + "." + s[-3:]
        elif len(s) <= 9:
            return s[:-6] + "." + s[-6:-3] + "." + s[-3:]
        else:
            return s[:-9] + "." + s[-9:-6] + "." + s[-6:-3] + "." + s[-3:]
