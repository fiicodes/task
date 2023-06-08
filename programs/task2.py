class Solution:
    def __init__(self, numbers):
        self.numbers = numbers

    def generate_cubes(self):
        return [num**3 for num in self.numbers]

generator = Solution([1, 2, 3, 4, 5,6])
result = generator.generate_cubes()
print(result)

