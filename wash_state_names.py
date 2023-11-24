import pandas as pd

from paths import (
    DATA_PATH,
    WASHED_DATA_PATH,
    STATE_PATHS
)
from utils import (
    remove_quotes,
    write_to_csv
)

"""
    Wash the state names of the district wise datasets.
    The state name of all districts in Telegana will be changes to Telengana.
"""

TELENGANA_DISTRICTS = [
    "adilabad",
    "bhadradri kothagudem",
    "hanamkonda",
    "hyderabad",
    "jagtial",
    "jangaon",
    "jayashankar bhupalpally",
    "jogulamba gadwal",
    "kamareddy",
    "karimnagar",
    "khammam",
    "kumuram bheem asifabad",
    "mahabubabad",
    "mahabubnagar",
    "mancherial",
    "medak",
    "medchal-malkajgiri",
    "mulugu",
    "nagarkurnool",
    "nalgonda",
    "narayanpet",
    "nirmal",
    "nizamabad",
    "peddapalli",
    "rajanna sircilla",
    "ranga reddy",
    "sangareddy",
    "siddipet",
    "suryapet",
    "vikarabad",
    "wanaparthy",
    "warangal",
    "yadadri bhuvanagiri"
]


for file_path in STATE_PATHS:
    path = f"{DATA_PATH}{file_path}"

    df = pd.read_csv(path)

    remove_quotes(df)

    for district in TELENGANA_DISTRICTS:
        df.loc[df['DISTRICT'].str.contains(district, case=False), 'STATE/UT'] = 'TELANGANA'
    
    df = df[~df['DISTRICT'].str.contains('total', case=False)]

    write_to_csv(df, f"{WASHED_DATA_PATH}washed_state_name_{file_path}")
