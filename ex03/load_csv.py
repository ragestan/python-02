import pandas as pd


def load(path: str):
    """
    Load a CSV file, print its dimensions, and return the dataset.

    This function reads a CSV file using pandas, validates the input,
    checks if the dataset is not empty, and prints the shape/dimensions
    in the format "Loading dataset of dimensions (rows, cols)".

    Args:
        path (str): Path to the CSV file to load.

    Returns:
        pd.DataFrame: The loaded dataset if successful, None otherwise.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.ParserError: If the CSV format is invalid.
        Exception: For any other unexpected errors during loading.
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
