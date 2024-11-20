class Median:
    # The Median class is responsible for calculating the median of a given dataset.
    # The median is the middle value in a sorted list of numbers. If the list has an odd number of elements,
    # the median is the value at the center. If the list has an even number of elements, the median is the
    # average of the two middle values.

    @staticmethod
    def calculate(data):
        # This static method calculates the median of the provided dataset (data).

        sorted_data = sorted(data)  # Sort the data in ascending order.
        n = len(sorted_data)  # Get the number of elements in the sorted data.
        mid = n // 2  # Find the index of the middle element (integer division).

        # If the number of elements is even, the median is the average of the two middle values.
        if n % 2 == 0:
            # For even length data, take the two middle elements and calculate their average.
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            # For odd length data, return the middle element.
            return sorted_data[mid]
