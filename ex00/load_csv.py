import pandas as pd


def load(path: str):
    """
    Load a CSV file, print its dimensions, and return the dataset.

    Args:
        path: Path to the CSV file

    Returns:
        pandas DataFrame if successful, None if error
    """
    try:
        # STEP 1: Check if path is valid string
        if not isinstance(path, str):
            print(f"Error: Path must be a string")
            return None

        # STEP 2: Try to read the CSV
        dataset = pd.read_csv(path)

        # STEP 3: Check if dataset is empty
        if dataset.empty:
            print(f"Error: Dataset is empty")
            return None

        # STEP 4: Get dimensions
        rows, cols = dataset.shape

        # STEP 5: Print dimensions
        print(f"Loading dataset of dimensions ({rows}, {cols})")

        # STEP 6: Return the dataset
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
