class Solution:
    def fib(self, N: int) -> int:
        if not N:
            return 0
        before_two = 0
        before_one = 1
        for _ in range(N-1):
            before_one, before_two = before_one+before_two, before_one
        return before_one


if __name__=="__main__":
    su = Solution()

    print(su.fib(3))