import pandas as pd

from paths import (
    WASHED_DATA_PATH,
    DISTRICT_WISE_CRIMES_AGAINST_WOMEN
)
from utils import (
    add_total_crimes,
    write_to_csv
)


df = pd.read_csv(f"{WASHED_DATA_PATH}washed_state_name_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")

crimes_df = df.drop(columns=[
    "STATE/UT",
    "DISTRICT",
    "Year"
])

add_total_crimes(df, crimes_df)

write_to_csv(df, f"{WASHED_DATA_PATH}washed_total_crimes_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")
