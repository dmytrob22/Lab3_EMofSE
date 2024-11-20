import random


class DataGenerator:
    # The DataGenerator class is responsible for generating a sequence of random numbers
    # based on the size provided (n). The numbers are randomly selected from 1 to (n+1).

    def __init__(self, n):
        self.n = n  # Store the value of 'n'
        self.data = []  # Initialize an empty list to store the generated data

    def generate_data(self):
        # This method generates a list of random integers based on the range 1 to (n+1)
        # and the total number of elements (n + 10).

        max_value = self.n + 1
        num_elements = self.n + 10

        self.data = [random.randint(1, max_value) for _ in range(num_elements)]

    def get_data(self):
        return self.data
