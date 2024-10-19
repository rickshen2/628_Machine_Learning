import polars as pl

# Sample DataFrame
df = pl.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6]
})

# Function to add a new column
def add_column(dataframe, new_col_name, value):
    return dataframe.with_columns(pl.lit(value).alias(new_col_name))

# Using pipe to apply the function
result_df = df.pipe(add_column, "c", 10)

print(result_df)
