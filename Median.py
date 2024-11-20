class Median:
    # The Median class is responsible for calculating the median of a given dataset.
    # The median is the middle value in a sorted list of numbers. If the list has an odd number of elements,
    # the median is the value at the center. If the list has an even number of elements, the median is the
    # average of the two middle values.

    @staticmethod
    def calculate(data):
        # This static method calculates the median of the provided dataset (data).

        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        # If the number of elements is even, the median is the average of the two middle values.
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) * 1.0 / 2
        else:
            return sorted_data[mid]
