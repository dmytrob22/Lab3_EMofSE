from collections import Counter  # Importing Counter from collections to count occurrences of elements in the data


class Mode:
    # The Mode class is responsible for calculating the mode(s) of a given dataset.
    # The mode is the value(s) that appear most frequently in the data.

    @staticmethod
    def calculate(data):
        # This static method calculates the mode(s) of the provided dataset (data).

        counts = Counter(data)  # Count the occurrences of each value in the data using Counter.
        max_count = max(counts.values())  # Find the highest frequency (the maximum count of occurrences).

        # Create a list of values (modes) that have the same frequency as the highest frequency (max_count).
        modes = [value for value, count in counts.items() if count == max_count]

        # If there is exactly one mode, return that mode.
        # If there are multiple modes (in case of a tie), return all modes as a list.
        return modes[0] if len(modes) == 1 else modes  # Return either a single mode or a list of modes.
