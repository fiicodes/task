class Solution:
    def __init__(self, numbers):
        self.numbers = numbers

    def concatenate_numbers(self):
        concatenated_string = ";".join(map(str, self.numbers[1:-1]))
        return concatenated_string


concatenator = Solution([1, 2, 3, 4, 5])
result = concatenator.concatenate_numbers()
print(result)

