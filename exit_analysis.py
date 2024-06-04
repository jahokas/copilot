import pandas as pd
import numpy as np
# create a dataframe df
df = pd.DataFrame({
    'Date': ['2024-05-08', '2024-01-09', '2024-02-12', '2024-02-16', '2024-05-12', '2024-05-08', '2024-01-09', '2024-02-12', '2024-03-16', '2024-05-12'],
    'CustomerID': ['001', '001', '001', '001', '001', '002', '002', '002', '002', '002'],
    'Status': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
})
# convert Date to datetime64[ns]
df['Date'] = pd.to_datetime(df['Date'])
# Create a new column 'YY-MM' that contains the year and month of the 'Date' column in the format 'YYYY-MM'
df['YY-MM'] = df['Date'].dt.strftime('%Y-%m')
# Reorder columns in df in the following order: 'Date', 'YY-MM', 'CustomerID', ''Status'
# print the dataframe df
print(df)
# print the data types of each column in df
# print(df.dtypes)
# sort values by the column 'Date' in ascending order and reset the index of the dataframe and drop the old index and print the dataframe
df = df.sort_values('Date').reset_index(drop=True)
# print(df)
# Group dataframe df by 'CustomerID', 'YY-MM' and take only the last row of each group and print the resulting dataframe
df_grouped = df.groupby(['CustomerID', 'YY-MM']).last().reset_index()
print(df_grouped)
# Create a function called 'inner_fill' that takes a dataframe as input and makes the following tasks:
# 1. Create an empthy list new_rows
# 2. Create grouped data set that enable to iterate through each group of rows that have the same combination of values for the columns: 'CustomerID'
# 3. Calculates the number of rows in the grouped data set and store it in the variable 'group_size'
# 4. If the 'group_size' is more than 1
# 5. Iterate 'i' through the range of 'group_size' - 1: for i in range(group_size - 1):
# 6. Calculate start_date and end_date: start_date is the first value in the 'YY-MM' column and end_date is the 'YY-MM' in the subsequent row, all in the format 'YYYY-MM' strftime('%Y-%m')
# 7. print start_date and end_date
# 8. calculate missing_dates = pd.date_range(min_date, max_date, freq='M').to_period('M').strftime('%Y-%m')
# 9. Exclude the first date in missing_dates if it is the same as the start_date missing_dates = missing_dates[1:]
# 10. for date in missing_dates:
# 11. Append the list new_rows with a new row that has the following values: 'CustomerID' is the same as the group, 'YY-MM' is date, 'Status' and 'Date' are the same as the first row in the group
# 12. Continue iterating through the groups and rows
# 13. Create a new dataframe new_df that is the concatenation of the input dataframe and the new_rows list
# 14. Return the new_df
def inner_fill(df):
    new_rows = []
    for name, group in df.groupby('CustomerID'):
        group_size = len(group)
        if group_size > 1:
            for i in range(group_size - 1):
                start_date = group['YY-MM'].iloc[i]
                end_date = group['YY-MM'].iloc[i + 1]
                missing_dates = pd.date_range(start_date, end_date, freq='ME').to_period('M').strftime('%Y-%m')
                missing_dates = missing_dates[1:]
                print(missing_dates)
                for date in missing_dates:
                    new_rows.append({'CustomerID': group['CustomerID'].iloc[0], 'YY-MM': date, 'Date': group['Date'].iloc[i], 'Status': group['Status'].iloc[i]})
    new_df = pd.concat([df, pd.DataFrame(new_rows)])
    return new_df
# Apply the function inner_fill to the dataframe df and print the resulting dataframe
df_filled = inner_fill(df_grouped)
df_filled = df_filled.sort_values(['CustomerID', 'Date']).reset_index(drop=True)
print(df_filled)
# print df_filled dtypes
# print(df_filled.dtypes)
# Expected output:
#     CustomerID    YY-MM       Date  Status
# 0         001  2024-01 2024-01-09       1
# 1         001  2024-02 2024-02-16       1
# 2         001  2024-03 2024-02-16       1
# 3         001  2024-04 2024-02-16       1
# 4         001  2024-05 2024-05-12       1
# create a test Expected output
df_expected = pd.DataFrame({
    'CustomerID': ['001', '001', '001', '001', '001', '002', '002', '002', '002', '002'],
    'YY-MM': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-01', '2024-02', '2024-03', '2024-04', '2024-05'],
    'Date': ['2024-01-09', '2024-02-16', '2024-02-16', '2024-02-16', '2024-05-12', '2024-01-09', '2024-02-16', '2024-03-16', '2024-03-16', '2024-05-12'],
    'Status': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
})
# convert Date to datetime64[ns]
df_expected['Date'] = pd.to_datetime(df_expected['Date'])
print(df_expected)
# print(df_expected.dtypes)   
assert df_filled.equals(df_expected), 'Test failed!'
print('Test passed!')
