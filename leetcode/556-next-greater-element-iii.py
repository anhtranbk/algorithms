class Solution:
    def numberToDigits(self, n):
        digits = []
        while n > 0:
            x, y = divmod(n, 10)
            digits.append(y)
            n = x
        return digits

    def digitsToNumber(self, digits):
        max_int = 2147483647
        n = 0
        for d in reversed(digits):
            n = n * 10 + d
        return n

    def nextGreaterElement(self, n: int) -> int:
        digits = self.numberToDigits(n)
        stack, mi = [], -1
        for i, d in enumerate(digits):
            while stack and d < digits[stack[-1]]:
                j = stack.pop()
                if mi < 0 or digits[j] < digits[mi]:
                    mi = j
            stack.append(i)
            if mi >= 0:
                digits[i], digits[mi] = digits[mi], digits[i]
                for j in range(i):
                    for k in range(j+1, i):
                        if digits[k] > digits[j]:
                            digits[j], digits[k] = digits[k], digits[j]
                break
        if mi < 0:
            return -1
        return self.digitsToNumber(digits)


if __name__ == '__main__':
    ret = MedianSortedArrays().nextGreaterElement(12443322)
    print(ret)
