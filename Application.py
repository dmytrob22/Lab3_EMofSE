from DataGenerator import DataGenerator
from Display import Display
from Mean import Mean
from Median import Median
from Mode import Mode


class Application:
    # The Application class serves as the main driver for generating data and calculating the statistical values.
    # It generates a sequence of data, calculates the Mode, Mean, and Median, and displays the results.

    def __init__(self, n):
        self.n = n

    def run(self):
        # The run method is the main entry point for the application logic.

        # Generate data
        generator = DataGenerator(self.n)
        generator.generate_data()
        data = generator.get_data()

        # Calculate Mode, Mean, and Median
        mode = Mode.calculate(data)
        mean = Mean.calculate(data)
        median = Median.calculate(data)

        # Display results
        Display.display_results(data, mode, mean, median)
