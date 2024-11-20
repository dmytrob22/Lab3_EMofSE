from collections import Counter


class Mode:
    # The Mode class is responsible for calculating the mode(s) of a given dataset.
    # The mode is the value(s) that appear most frequently in the data.

    @staticmethod
    def calculate(data):
        # This static method calculates the mode(s) of the provided dataset (data).

        counts = Counter(data)
        max_count = max(counts.values())

        modes = [value for value, count in counts.items() if count == max_count]

        return modes[0] if len(modes) == 1 else modes
