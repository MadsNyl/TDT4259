import pandas as pd

from paths import (
    DATA_PATH,
    SUM_DATA,
    TYPE_OF_CRIME_AGAINST_WOMEN
)

# Read the input CSV file
df = pd.read_csv(f"{DATA_PATH}{TYPE_OF_CRIME_AGAINST_WOMEN}", on_bad_lines="skip")

# Select the columns to sum
columns_to_sum = [
    # 'Cases_Chargesheeted',
    'Cases_Sent_for_Trial',
    'Cases_Pending_Trial_at_Year_End',
    'Cases_Pending_Trial_from_the_previous_year',
    "Total_Cases_for_Trial"
]

# Group the data by year and sum the values for each year
sum_by_year = df.groupby('Year', as_index=False)[columns_to_sum].sum()

# Select the first 5 rows
sum_by_year = sum_by_year.head(5)

print(sum_by_year)



# Select all crime columns
# crime_columns = df.drop(columns=[
#     "STATE/UT",
#     "DISTRICT",
#     "Year",
#     "total_crimes"
# ]).columns

# # Group the data by year and sum the values for each year
# sum_by_year = df.groupby('Year', as_index=False)[crime_columns].sum()

# # Save the resulting dataframe to a new CSV file
# sum_by_year.to_csv(f"{SUM_DATA}sum_for_each_year_{TYPE_OF_CRIME_AGAINST_WOMEN}", index=False)
