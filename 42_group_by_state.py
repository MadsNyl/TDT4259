import pandas as pd

from paths import (
    WASHED_DATA_PATH,
    DISTRICT_WISE_CRIMES_AGAINST_WOMEN
)
from utils import write_to_csv


df = pd.read_csv(f"{WASHED_DATA_PATH}washed_total_crimes_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")

df.drop(columns=[
    "DISTRICT"
])

df = df.groupby(["STATE/UT", "Year"], as_index=False).sum(numeric_only=True)

write_to_csv(df, f"{WASHED_DATA_PATH}washed_grouped_by_state_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")