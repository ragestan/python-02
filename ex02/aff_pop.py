from load_csv import load

import matplotlib.pyplot as plt
import pandas as pd


def _to_millions(value: str | float | int) -> float | None:
	if pd.isna(value):
		return None
	if isinstance(value, (int, float)):
		return float(value)
	text = str(value).strip()
	if text == "":
		return None
	multiplier = 1.0
	if text.endswith("k"):
		multiplier = 1e-3
		text = text[:-1]
	elif text.endswith("M"):
		multiplier = 1.0
		text = text[:-1]
	elif text.endswith("B"):
		multiplier = 1e3
		text = text[:-1]
	try:
		return float(text) * multiplier
	except ValueError:
		return None


def main():
	dataset = load("population_total.csv")
	if dataset is None:
		return

	countries = ["Morocco", "France"]
	country_data = dataset[dataset["country"].isin(countries)]
	if country_data.empty or country_data["country"].nunique() < 2:
		print("Error: Morocco or France not found in dataset")
		return

	years = pd.to_numeric(dataset.columns[1:], errors="coerce")
	mask = (years >= 1800) & (years <= 2050)

	for country in countries:
		row = country_data[country_data["country"] == country]
		values = pd.to_numeric(row.iloc[0, 1:].apply(_to_millions), errors="coerce")
		plt.plot(years[mask], values[mask], label=country)

	plt.title("Population: Morocco vs France")
	plt.xlabel("Year")
	plt.ylabel("Population (millions)")
	plt.legend()
	plt.xlim(1800, 2050)
	plt.xticks(range(1800, 2051, 40), rotation=45)
	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
