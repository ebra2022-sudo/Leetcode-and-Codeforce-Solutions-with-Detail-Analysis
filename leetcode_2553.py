class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        concatinated_digits = []
        for num in nums:
            current_num = num
            current_digits = []
            while current_num > 0:
                current_digits.append(current_num % 10)
                current_num //= 10 
            current_digits.reverse()
            concatinated_digits += current_digits

        return concatinated_digits



