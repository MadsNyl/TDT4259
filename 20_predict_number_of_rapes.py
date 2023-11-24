import pandas as pd

import numpy as np

from sklearn.linear_model import LinearRegression

from paths import (
    PREDICTED_DATA_PATH,
    WASHED_DATA_PATH,
    VICTIMS_OF_RAPE
)
from utils import (
    write_to_csv,
    add_total_crimes
)


NUMERICAL_COLUMNS = [
    "Rape_Cases_Reported",
    "Victims_Above_50_Yrs",
    "Victims_Between_10-14_Yrs",
    "Victims_Between_14-18_Yrs",
    "Victims_Between_18-30_Yrs",
    "Victims_Between_30-50_Yrs",
    "Victims_Upto_10_Yrs"
]


df = pd.read_csv(f"{WASHED_DATA_PATH}washed_grouped_by_total_{VICTIMS_OF_RAPE}")

df = df.drop(columns=["Subgroup", "Victims_of_Rape_Total"])

# Create a new dataframe with all the combinations of states and years
states = df["Area_Name"].unique()
years = np.arange(2001, 2025)

all_combinations = [(state, year) for state in states for year in years]
new_df = pd.DataFrame(all_combinations, columns=['Area_Name', 'Year'])

# Merge the two dataframes with existing values
merged_df = new_df.merge(df, on=['Area_Name', 'Year'], how='left')
merged_df.fillna(0, inplace=True)

# Predict the values for the missing years
predicted_values = {}

grouped_df = merged_df.groupby('Area_Name')

for state, group in grouped_df:
    X = group['Year'].values.reshape(-1, 1)
    for column in NUMERICAL_COLUMNS:
        y = group[column].values.reshape(-1, 1)
        model = LinearRegression()
        model.fit(X[:10], y[:10])
        predicted_values[(state, column)] = model.predict(X[10:])
        
        # Add the predicted values to the dataframe
        merged_df.loc[(merged_df['Area_Name'] == state) & (merged_df['Year'] >= 2011), column] = predicted_values[(state, column)].flatten()

# Convert floats to integers
for column in NUMERICAL_COLUMNS:
    merged_df[column] = merged_df[column].astype(int)

# Add the total number of crimes
add_total_crimes(merged_df, merged_df[NUMERICAL_COLUMNS], name="total rapes")

# Write the dataframe to a csv file
write_to_csv(merged_df, f"{PREDICTED_DATA_PATH}predicted_number_of_rapes_2024_{VICTIMS_OF_RAPE}")
