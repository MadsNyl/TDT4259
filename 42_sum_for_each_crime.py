import pandas as pd

from paths import (
    WASHED_DATA_PATH,
    SUM_DATA,
    DISTRICT_WISE_CRIMES_AGAINST_WOMEN
)

# Read the input CSV file
df = pd.read_csv(f"{WASHED_DATA_PATH}washed_total_crimes_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")

# Select all crime columns
crime_columns = df.drop(columns=[
    "STATE/UT",
    "DISTRICT",
    "Year",
    "total_crimes"
]).columns

# Group the data by year and sum the values for each year
sum_by_year = df.groupby('Year', as_index=False)[crime_columns].sum()

# Save the resulting dataframe to a new CSV file
sum_by_year.to_csv(f"{SUM_DATA}sum_for_each_year_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}", index=False)
