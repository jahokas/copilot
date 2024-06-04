import pandas as pd
import numpy as np
import datetime
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
df_grouped = df.groupby(['CustomerID']).last().reset_index()
print(df_grouped)
# Create a function called 'extention' that takes a dataframe as input and makes the following tasks:
# 1. Create an empthy list new_rows
# 2. calculate the current date in the format 'YYYY-MM' strftime('%Y-%m') and assign it to the variable 'end_date'
# 3. Group the input dataframe by 'CustomerID' and orders the groups by 'YY-MM' in ascending order and takes only the last row of each group
# 4. calculate the minimum date in the 'YY-MM' column and assign it to the variable 'start_date'
# 5. print start_date and end_date
# 8. calculate missing_dates = pd.date_range(start_date, end_date, freq='M').to_period('M').strftime('%Y-%m')
# 9. Exclude the first date in missing_dates if it is the same as the start_date missing_dates = missing_dates[1:]
# 10. for date in missing_dates:
# 11. Append the list new_rows with a new row that has the following values: 'CustomerID' is the same as the group, 'YY-MM' is date, 'Status' and 'Date' are the same as the first row in the group
# 12. Continue iterating through the groups and rows
# 13. Create a new dataframe new_df that is the concatenation of the input dataframe and the new_rows list
# 14. Return the new_df
def extention(df):
    new_rows = []
    end_date = datetime.datetime.now().strftime('%Y-%m')
    df = df.sort_values(['CustomerID', 'YY-MM']).reset_index(drop=True)
    df_last = df.groupby(['CustomerID']).last()
    for name, group in df_last.groupby('CustomerID'):
        start_date = group['YY-MM'].min()
        missing_dates = pd.date_range(start_date, end_date, freq='ME').to_period('M').strftime('%Y-%m')
        missing_dates = missing_dates[1:]
        for date in missing_dates:
            new_rows.append({'CustomerID': name, 'YY-MM': date, 'Status': group['Status'].iloc[0], 'Date': group['Date'].iloc[0]})
    new_df = pd.concat([df, pd.DataFrame(new_rows)])
    return new_df
# Apply the function 'extention' to the dataframe df and print the resulting dataframe
df_extended = extention(df).sort_values(['CustomerID', 'YY-MM']).reset_index(drop=True)
print(df_extended)