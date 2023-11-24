import pandas as pd

from paths import (
    DATA_PATH,
    WASHED_DATA_PATH,
    NOT_MURDER_VICTIM_AGE_SEX
)
from utils import write_to_csv


# Read in original dataframe
df = pd.read_csv(f"{DATA_PATH}{NOT_MURDER_VICTIM_AGE_SEX}")

# Create new dataframe with only rows where gender is "woman"
women_df = df[df["Sub_Group_Name"] == "2. Female Victims"]

# Write to csv
write_to_csv(women_df, f"{WASHED_DATA_PATH}washed_filter_out_women_{NOT_MURDER_VICTIM_AGE_SEX}")