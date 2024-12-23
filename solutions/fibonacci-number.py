class Solution:
    def fib(self, n: int) -> int:
        return 0 if n == 0 else 1 if n == 1 else self.fib(n-1) + self.fib(n-2)


# нашел
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b