import pandas as pd

from paths import (
    DATA_PATH,
    WASHED_DATA_PATH,
    OFFENDERS_KNOWN_TO_VICTIM
)
from utils import (
    add_total_crimes,
    remove_quotes,
    write_to_csv
)


df = pd.read_csv(f"{DATA_PATH}{OFFENDERS_KNOWN_TO_VICTIM}")

remove_quotes(df)

crimes_df = df.drop(columns=[
    "Area_Name",
    "Year"
])

add_total_crimes(df, crimes_df)

write_to_csv(df, f"{WASHED_DATA_PATH}washed_total_crimes_{OFFENDERS_KNOWN_TO_VICTIM}")
