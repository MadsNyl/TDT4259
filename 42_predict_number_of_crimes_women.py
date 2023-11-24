import pandas as pd

import numpy as np

from sklearn.linear_model import LinearRegression

from paths import (
    PREDICTED_DATA_PATH,
    WASHED_DATA_PATH,
    DISTRICT_WISE_CRIMES_AGAINST_WOMEN
)
from utils import (
    write_to_csv,
    add_total_crimes
)


NUMERICAL_COLUMNS = [
    "Rape",
    "Kidnapping and Abduction",
    "Dowry Deaths",
    "Assault on women with intent to outrage her modesty",
    "Insult to modesty of Women",
    "Cruelty by Husband or his Relatives",
    "Importation of Girls"
]


df = pd.read_csv(f"{WASHED_DATA_PATH}washed_grouped_by_state_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")

# Create a new dataframe with all the combinations of states and years
states = df["STATE/UT"].unique()
years = np.arange(2001, 2025)

all_combinations = [(state, year) for state in states for year in years]
new_df = pd.DataFrame(all_combinations, columns=['STATE/UT', 'Year'])

# Merge the two dataframes with existing values
merged_df = new_df.merge(df, on=['STATE/UT', 'Year'], how='left')
merged_df.fillna(0, inplace=True)

# Predict the values for the missing years
predicted_values = {}

grouped_df = merged_df.groupby('STATE/UT')

for state, group in grouped_df:
    X = group['Year'].values.reshape(-1, 1)
    for column in NUMERICAL_COLUMNS:
        y = group[column].values.reshape(-1, 1)
        model = LinearRegression()
        model.fit(X[:12], y[:12])
        predicted_values[(state, column)] = model.predict(X[12:])
        
        # Add the predicted values to the dataframe
        merged_df.loc[(merged_df['STATE/UT'] == state) & (merged_df['Year'] >= 2013), column] = predicted_values[(state, column)].flatten()

# Convert floats to integers
for column in NUMERICAL_COLUMNS:
    merged_df[column] = merged_df[column].astype(int)

# Add total crimes to the dataframe
add_total_crimes(merged_df, merged_df[NUMERICAL_COLUMNS])

# Save the predicted data to a csv file
write_to_csv(merged_df, f"{PREDICTED_DATA_PATH}predicted_crimes_2024_{DISTRICT_WISE_CRIMES_AGAINST_WOMEN}")
