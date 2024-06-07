import pandas as pd
import os

# Directory containing the Excel files
folder_path = r'C:\Users\hardy\OneDrive - Institut Teknologi Sepuluh Nopember\Desktop\datatweet'

# List to store dataframes
df_list = []

# Iterate through all Excel files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv') or filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        df_list.append(df)

# Concatenate all dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new Excel file
combined_df.to_excel('combined_file.xlsx', index=False)

print("All files have been successfully combined into combined_file.xlsx")
