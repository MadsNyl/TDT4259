import pandas as pd

from paths import (
    WASHED_DATA_PATH,
    SUM_DATA,
    MURDER_VICTIM_AGE_SEX
)


# Read the csv file
df = pd.read_csv(f"{WASHED_DATA_PATH}washed_filter_out_women_{MURDER_VICTIM_AGE_SEX}")

# Change all NaN values to 0
df.fillna(0, inplace=True)

# Change all floats to Integers
df = df.apply(lambda x: x.astype(int) if x.dtype == float else x)

# Drop all values to not be summed
sum_columns = df.drop(columns=[
    "Area_Name",
    "Year",
    "Group_Name",
    "Sub_Group_Name"
]).columns

# Group the data by year and sum the values for each year
sum_by_year = df.groupby('Year', as_index=False)[sum_columns].sum()

# Save the resulting dataframe to a new CSV file
sum_by_year.to_csv(f"{SUM_DATA}sum_for_each_year_{MURDER_VICTIM_AGE_SEX}", index=False)