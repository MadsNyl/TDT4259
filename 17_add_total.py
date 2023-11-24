import pandas as pd

from paths import (
    DATA_PATH,
    WASHED_DATA_PATH,
    PLACE_OF_OCCURRENCES
)
from utils import (
    add_total_crimes,
    remove_quotes,
    write_to_csv
)


df = pd.read_csv(f"{DATA_PATH}{PLACE_OF_OCCURRENCES}")

remove_quotes(df)

crimes_df = df.drop(columns=[
    "STATE/UT",
    "YEAR",
    "TOTAL - Dacoity",
    "TOTAL - Robbery",
    "TOTAL - Burglary",
    "TOTAL - Theft"
])

add_total_crimes(df, crimes_df)

write_to_csv(df, f"{WASHED_DATA_PATH}washed_total_crimes_{PLACE_OF_OCCURRENCES}")
