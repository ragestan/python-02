from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Analyze and visualize the relationship between GDP per capita and life \
expectancy for year 1900.
    """
    try:
        gdp_dataset = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_dataset = load("life_expectancy_years.csv")
        if gdp_dataset is None or life_dataset is None:
            return
        year = "1900"
        if year not in gdp_dataset.columns or year not in life_dataset.columns:
            print("Error: Year 1900 not found in dataset")
            return
        gdp_1900 = gdp_dataset[["country", year]].copy()
        life_1900 = life_dataset[["country", year]].copy()
        gdp_1900[year] = pd.to_numeric(gdp_1900[year], errors="coerce")
        life_1900[year] = pd.to_numeric(life_1900[year], errors="coerce")
        merged = gdp_1900.merge(
            life_1900, on="country", suffixes=("_gdp", "_life"))
        merged = merged.dropna(subset=[f"{year}_gdp", f"{year}_life"])
        plt.scatter(
            merged[f"{year}_gdp"], merged[f"{year}_life"], label="1900",
            alpha=0.7)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy (years)")
        plt.xscale("log")
        plt.xlim(300, 10000)
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.tight_layout()
        plt.show()
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except KeyError as e:
        print(f"Error: Key not found - {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
