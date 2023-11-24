import pandas as pd

from paths import (
    DATA_PATH,
    WASHED_DATA_PATH,
    VICTIMS_OF_RAPE
)
from utils import write_to_csv


df = pd.read_csv(f"{DATA_PATH}{VICTIMS_OF_RAPE}")

df = df[df["Subgroup"] == "Total Rape Victims"]

write_to_csv(df, f"{WASHED_DATA_PATH}washed_grouped_by_total_{VICTIMS_OF_RAPE}")