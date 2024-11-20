class Display:
    # The Display class is responsible for displaying the results of the statistical calculations.
    # It contains a static method to print the generated data and the calculated statistical values (Mode, Mean, Median).

    @staticmethod
    def display_results(data, mode, mean, median):
        # This static method prints the generated data and the calculated mode, mean, and median.

        print("Generated Data:")  # Print a header for the data
        print(data)  # Output the generated data sequence

        print("\nResults:")  # Print a header for the results
        # Display the Mode, Mean, and Median values with appropriate formatting.
        print(f"Mode: {mode}")  # Print the Mode (most frequent value or values)
        print(f"Mean: {mean:.2f}")  # Print the Mean with two decimal places
        print(f"Median: {median}")  # Print the Median (middle value or average of two middle values)
