import pandas as pd


def load(path: str):
    """
    Load a CSV file, print its dimensions, and return the dataset.
    """
    try:
        # Validate that path is a string
        if not isinstance(path, str):
            print("Error: Path must be a string")
            return None

        # Read the CSV file using pandas
        dataset = pd.read_csv(path)

        # Verify that the dataset is not empty
        if dataset.empty:
            print("Error: Dataset is empty")
            return None

        # Get the dimensions of the dataset
        rows, cols = dataset.shape

        # Print the dimensions
        print(f"Loading dataset of dimensions ({rows}, {cols})")

        # Return the loaded dataset
        return dataset

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except pd.errors.ParserError:
        print(f"Error: Invalid CSV format in '{path}'")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def main():
    """
    Main function to demonstrate the load function.
    """
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is not None:
            print(dataset)
    except Exception as e:
        print(f"Unexpected error in main: {str(e)}")


if __name__ == "__main__":
    main()
