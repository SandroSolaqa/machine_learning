import pandas as pd

# Read the Excel file
new_data = pd.read_excel("12hour_data.xlsx")
# new_data = pd.read_excel("15minute_data_california.xlsx")
# Drop columns with missing values
new_data.dropna(axis=1, inplace=True)

# Save the modified data to a new Excel file
new_data.to_excel('new_file.xlsx', index=False)
