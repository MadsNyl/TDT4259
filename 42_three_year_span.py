import pandas as pd

from paths import (
    SUM_DATA,
    DISTRICT_WISE_CRIMES_AGAINST_WOMEN   
)

from utils import write_to_csv


# Read csv file
df = pd.read_csv(f"{SUM_DATA}sum_for_each_year_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")

# Create new dataframe with last three rows
three_years_df = df.tail(3)

# Write to csv
write_to_csv(three_years_df, f"{SUM_DATA}sum_for_last_three_years_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")