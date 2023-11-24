import pandas as pd

from paths import (
    SUM_DATA,
    MURDER_VICTIM_AGE_SEX,
    NOT_MURDER_VICTIM_AGE_SEX
)


# Read the murder CSV file
murder_df = pd.read_csv(f"{SUM_DATA}sum_for_each_year_{MURDER_VICTIM_AGE_SEX}")

# Read the not murder CSV file
not_murder_df = pd.read_csv(f"{SUM_DATA}sum_for_each_year_{NOT_MURDER_VICTIM_AGE_SEX}")

# Merge the two dataframes
merged_df = pd.concat([not_murder_df, murder_df])
merged_df = merged_df.groupby("Year").sum().reset_index()

# Write the merged dataframe to a new CSV file
merged_df.to_csv(f"{SUM_DATA}merged_sum_32-33_victims_by_age.csv", index=False)
