import pandas as pd

# Load the CSV data into a pandas DataFrame
data  = pd.read_csv("./filtered_location_empty.csv")

# Drop the 'keyword' and 'target' columns
df_cleaned = data.drop(columns=['keyword', 'target'])

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv("./filtered_location_empty.csv", index=False)
