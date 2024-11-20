class Display:

    @staticmethod
    def display_results(data, mode, mean, median):

        print("Generated Data:")
        print(data)
        print("Sorted Data:")
        print(sorted(data))

        print("\nResults:")

        print(f"Mode: {mode}")
        print(f"Mean: {mean:.2f}")
        print(f"Median: {median}")
