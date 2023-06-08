class Solution:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        return list(range(1, self.n+1))

generator = Solution(10)
result = generator.generate_numbers()
print(result)

