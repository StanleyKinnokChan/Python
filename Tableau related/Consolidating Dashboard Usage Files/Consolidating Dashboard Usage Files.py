import os
import pandas as pd

# Directory containing the CSV files
directory = r'C:\Users\schan4\Downloads'
 
# Initialize an empty list to hold dataframes
dataframes = []
 
# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the filename contains 'Who Has Seen' and ends with '.csv'
    if 'Who Has Seen' in filename and filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)
        # Read the CSV file into a DataFrame
        sheet_name=filename.replace(".xlsx","")
        df = pd.read_excel(file_path,sheet_name="Sheet 1")
        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
consolidated_df = pd.concat(dataframes, ignore_index=True)
 
# Output path for the consolidated CSV file
output_path = os.path.join(directory, 'consolidated_who_has_seen.csv')
 
# Save the consolidated DataFrame to a new CSV file
consolidated_df.to_csv(output_path, index=False)
 
print(f"Consolidated CSV file has been saved to {output_path}")