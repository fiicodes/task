class Solution:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse_list(self):
        return self.input_list[::-1]

reverser = Solution([1, 2, 3, 4, 5])
result = reverser.reverse_list()
print(result)

