from DataGenerator import DataGenerator  # Import the DataGenerator class to generate the dataset
from Display import Display  # Import the Display class to show results
from Mean import Mean  # Import the Mean class to calculate the mean
from Median import Median  # Import the Median class to calculate the median
from Mode import Mode  # Import the Mode class to calculate the mode


class Application:
    # The Application class serves as the main driver for generating data and calculating the statistical values.
    # It generates a sequence of data, calculates the Mode, Mean, and Median, and displays the results.

    def __init__(self, n):
        # The constructor initializes the application with a parameter 'n', which determines the size of the dataset.
        self.n = n

    def run(self):
        # The run method is the main entry point for the application logic.

        # Generate data
        generator = DataGenerator(self.n)  # Create an instance of DataGenerator with the specified size 'n'.
        generator.generate_data()  # Generate the data sequence.
        data = generator.get_data()  # Get the generated data sequence.

        # Calculate Mode, Mean, and Median
        mode = Mode.calculate(data)  # Calculate the Mode of the generated data.
        mean = Mean.calculate(data)  # Calculate the Mean of the generated data.
        median = Median.calculate(data)  # Calculate the Median of the generated data.

        # Display results
        Display.display_results(data, mode, mean, median)  # Display the generated data and the calculated statistical results.
