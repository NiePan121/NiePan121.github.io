import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Change working directory
os.chdir("C:/Users/lyu5/Desktop/IBI/Practical")
# Check current directory and files
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())
# Load dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("\n----- First 5 rows -----")
print(dalys_data.head(5))
print("\n----- Data info -----")
print(dalys_data.info())
print("\n----- Summary statistics -----")
print(dalys_data.describe())

# Task 1: First 10 rows, columns Year (2) and DALYs (3)
first_10_year_dalys = dalys_data.iloc[0:10, 2:4]
print("\n----- First 10 rows: Year + DALYs -----")
print(first_10_year_dalys)
# Afghanistan: max DALYs year in first 10 records
afghanistan_data = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"].head(10)
max_dalys_year_afghan = afghanistan_data.loc[afghanistan_data["DALYs"].idxmax(), "Year"]
print("\nAfghanistan: Year with max DALYs (first 10):", max_dalys_year_afghan)

# Task 2: Zimbabwe all years
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[is_zimbabwe]
print("\n----- Zimbabwe data -----")
print(zimbabwe_data)
# Zimbabwe first and last year
zimbabwe_first_year = zimbabwe_data["Year"].min()
zimbabwe_last_year = zimbabwe_data["Year"].max()
print("Zimbabwe first year:", zimbabwe_first_year)
print("Zimbabwe last year:", zimbabwe_last_year)

# Task 3: 2019 max and min DALYs countries
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_2019 = data_2019.loc[data_2019["DALYs"].idxmax()]
min_2019 = data_2019.loc[data_2019["DALYs"].idxmin()]
print("\n----- 2019 Max DALYs -----")
print(max_2019)
print("\n----- 2019 Min DALYs -----")
print(min_2019)

# Task 4: Plot time series for 2019 max country
max_country_name = max_2019["Entity"]
max_country_data = dalys_data.loc[dalys_data["Entity"] == max_country_name]
plt.figure()
plt.plot(max_country_data["Year"], max_country_data["DALYs"], "b+")
plt.xticks(max_country_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs Over Time: {max_country_name}")
plt.show()

# Task 5: Answer your own question
# Question: What is the distribution of DALYs across all countries in 2019?
plt.figure()
plt.hist(data_2019["DALYs"], bins=20)
plt.xlabel("DALYs (2019)")
plt.ylabel("Number of Countries")
plt.title("2019 Global DALYs Distribution")
plt.show()