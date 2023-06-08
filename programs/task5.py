class Solution:
    def __init__(self, number):
        self.number = number

    def reverse_number(self):
        reversed_number = int(str(self.number)[::-1])
        return reversed_number


reverser = Solution(12345)
result = reverser.reverse_number()
print(result)
