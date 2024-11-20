class Mean:
    # The Mean class is responsible for calculating the arithmetic mean (average) of a given dataset.

    @staticmethod
    def calculate(data):
        # This static method calculates the arithmetic mean of the provided dataset (data).

        return sum(data) / len(data)
