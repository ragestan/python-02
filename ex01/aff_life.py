from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Plot life expectancy for Morocco over time from 1800 to 2100.
    """
    try:
        # Load the life expectancy dataset
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            return

        # Filter dataset for Morocco only
        morocco_row = dataset[dataset["country"] == "Morocco"]
        if morocco_row.empty:
            print("Error: Morocco not found in dataset")
            return

        # Extract years and life expectancy values
        years = pd.to_numeric(dataset.columns[1:], errors="coerce")
        values = pd.to_numeric(morocco_row.iloc[0, 1:], errors="coerce")

        # Filter data for years 1800-2100
        mask = (years >= 1800) & (years <= 2100)

        # Create and display plot
        plt.plot(years[mask], values[mask])
        plt.title("Morocco life expectancy Projection")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xlim(1800, 2100)
        plt.xticks(range(1800, 2101, 40), rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Unexpected error in main: {str(e)}")


if __name__ == "__main__":
    main()