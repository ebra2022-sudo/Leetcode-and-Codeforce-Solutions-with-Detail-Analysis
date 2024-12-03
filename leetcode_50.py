"""
Problem Description(50. Pow(x, n)):

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution(object):
    # Naive Algorithm
    # this uses incremental approach (multiplication incremental) until it multiplies n times
    # so the time complexity is O(n)
    # space complexity of O(1) since it doesn't create new object or no call stack in it.

    def naive_pow(self, x, n):
        # Handle negative powers: if n is negative, make n positive and x is reciprocal of previous x.
        # since x^(-n) = (1 / x)^n
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n > 0:
            result *= x
            n -= 1
        return result

    # this method is based on divide and conquer method in recursive
    # with deeper recursion tree which leds to inefficient in memory usage even-though it is fast
    # time complexity is O(log(n))
    # space complexity O(H(n)) where H(n) is the height of the recursion tree which is depends on n
    """
            | log(n) if n is power of 2
    H(n) =  |   
            | n - 1 if n is odd and 
    """

    def recursive_pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        if n == 1:
            return x
        if n % 2 == 0:
            half_n = n / 2
            return self.recursive_pow(x, half_n) * self.recursive_pow(x, half_n)
        else:
            return self.recursive_pow(x, n - 1) * x

    # this uses divide and conquer using iterative method and this the most efficient one
    # time complexity is O(log(n))
    # space complexity of O(1)
    def iterative_pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        current_product = x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2

        return result


print(Solution().naive_pow(2, 10000))
print(Solution().recursive_pow(2, 10000))
print(Solution().iterative_pow(2, 10000))
