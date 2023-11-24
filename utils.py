

# Remove quotes from elements
def remove_quotes(df):
    df.applymap(lambda x: str(x).replace('"', ""))


# Add total crimes to df
def add_total_crimes(df, columns, name="total_crimes"):
    df[name] = columns.sum(axis=1)


# Write df to csv
def write_to_csv(df, file_name):
    df.to_csv(file_name, index=False)