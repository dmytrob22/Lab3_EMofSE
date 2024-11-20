import random  # Importing the random module to generate random numbers


class DataGenerator:
    # The DataGenerator class is responsible for generating a sequence of random numbers
    # based on the size provided (n). The numbers are randomly selected from 1 to (n+1).

    def __init__(self, n):
        # The constructor method initializes the instance with the size of data (n).
        # 'n' is the number of values used to determine the range (1 to n+1) and the number
        # of data elements to generate (n + 10).
        self.n = n  # Store the value of 'n'
        self.data = []  # Initialize an empty list to store the generated data

    def generate_data(self):
        # This method generates a list of random integers based on the range 1 to (n+1)
        # and the total number of elements (n + 10).

        max_value = self.n + 1  # Set the maximum value for the random integers as (n + 1)
        num_elements = self.n + 10  # The total number of random numbers to generate (n + 10)

        # Generate 'num_elements' random integers between 1 and 'max_value' and store them in 'data'
        self.data = [random.randint(1, max_value) for _ in range(num_elements)]

    def get_data(self):
        # This method returns the generated data list.
        return self.data
