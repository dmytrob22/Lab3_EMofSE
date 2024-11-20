class Mean:
    # The Mean class is responsible for calculating the arithmetic mean (average) of a given dataset.

    @staticmethod
    def calculate(data):
        # This static method calculates the arithmetic mean of the provided dataset (data).

        # The mean is calculated by dividing the sum of all elements in the data by the number of elements.
        return sum(data) / len(data)  # Return the mean (average) of the data.
