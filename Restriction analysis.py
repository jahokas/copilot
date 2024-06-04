# create a dataframe df that has the following columns: Date, CustomerID, Activity and Status
# Date should have the following values: '2024-04-08', '2024-02-09', '2024-03-12', '2024-03-16'
# CustomerID should have the following values: 001, 001, 001, 001
# Activity should have the following values: 'Restriction', 'Restriction', 'Restriction', 'Restriction'
# Status should have the following values: 0, 1, 1, 1
# Dates are dtype datetime64[ns], CustomerID are dtype object, Activity are dtype object, Status are dtype int64
# Print the dataframe df
# Print the data types of each column in df
import pandas as pd
import numpy as np
# create a dataframe df
df = pd.DataFrame({
    'Date': ['2024-05-08', '2024-01-09', '2024-02-12', '2024-02-16', '2024-05-12'],
    'CustomerID': ['001', '001', '001', '001', '001'],
    'Status': [1, 1, 1, 1, 1]
})
# convert Date to datetime64[ns]
df['Date'] = pd.to_datetime(df['Date'])
# Create a new column 'YY-MM' that contains the year and month of the 'Date' column in the format 'YYYY-MM'
df['YY-MM'] = df['Date'].dt.strftime('%Y-%m')
# Reorder columns in df in the following order: 'Date', 'YY-MM', 'CustomerID', ''Status'
# print the dataframe df
print(df)
# print the data types of each column in df
print(df.dtypes)
# sort values by the column 'Date' in ascending order and reset the index of the dataframe and drop the old index and print the dataframe
df = df.sort_values('Date').reset_index(drop=True)
print(df)
# Group dataframe df by 'CustomerID', 'YY-MM' and take only the last row of each group and print the resulting dataframe
df_grouped = df.groupby(['CustomerID', 'YY-MM']).last().reset_index()
print(df_grouped)
# Create a function called 'inner_fill' that takes a dataframe as input and makes the following tasks:
# 1. Create an empthy list new_rows
# 2. Create grouped data set that enable to iterate through each group of rows that have the same combination of values for the columns: 'CustomerID'
# 3. Calculates the number of rows in the grouped data set and store it in the variable 'group_size'
# 4. If the 'group_size' is more than 1
# 5. Iterate 'i' through the range of 'group_size' - 1
# 6. Calculate start_date and end_date: start_date is the first value in the 'YY-MM' column and end_date is the 'YY-MM' in the subsequent row
# 7. If the difference between end_date and start_date is more than 1 month
# 8. Append the list new_rows with a new row that has the following values: 'CustomerID' is the same as the group, 'YY-MM' is start_date after one month, 'Status' and 'Date' are the same as the first row in the group
# 9. Create a new dataframe new_df that is the concatenation of the input dataframe and the new_rows list
# 10. Return the new_df
def inner_fill(df):
    new_rows = []
    for name, group in df.groupby('CustomerID'):
        group_size = len(group)
        print(group_size)
        if group_size > 1:
            for i in range(group_size - 1):
                start_date = group['Date'].iloc[i].to_period('M').strftime('%Y-%m-%d')
                end_date = group['Date'].iloc[i + 1].to_period('M').strftime('%Y-%m-%d')
                print(start_date, end_date)
                days_diff = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
                print(days_diff)
                while days_diff > 30:
                    new_rows.append({'CustomerID': group['CustomerID'].iloc[0], 'YY-MM': group['YY-MM'].iloc[i+1], 'Date': group['Date'].iloc[i], 'Status': group['Status'].iloc[i+1]})
                    days_diff -= 30
    new_df = pd.concat([df, pd.DataFrame(new_rows)])
    return pd.DataFrame(new_rows)
# Apply the function inner_fill to the dataframe df and print the resulting dataframe
df_filled = inner_fill(df_grouped)
print(df_filled)
