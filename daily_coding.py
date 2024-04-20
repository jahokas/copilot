import pandas as pd
import random

# Create a list of random years between 2021 and 2023
years = [random.randint(2021, 2023) for _ in range(20)]

# Create a list of random strings 'restricted' or 'terminated'
statuses = [random.choice(['restricted', 'terminated']) for _ in range(20)]

# Create a list of random integers between 1 and 10
numbers = [random.randint(1, 10) for _ in range(20)]

# Create the DataFrame
df = pd.DataFrame({'Year': years, 'Status': statuses, 'Number': numbers})

# Convert 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Sort rows based on 'Year' column in ascending order
df = df.sort_values('Year')

df = df.reset_index(drop=True)

# Group the DataFrame by 'Year' and 'Status' columns and calculate sum of 'Number'
grouped_df = df.groupby(['Year', 'Status']).sum('Number')

# Calculate the total sum of 'Number' column
total_sum = df['Number'].sum()

# Add the total sum as the last row to the grouped DataFrame
grouped_df.loc[('Total', 'Total'), 'Number'] = total_sum

# Reset the index of the grouped DataFrame
grouped_df = grouped_df.reset_index()

# Print the updated DataFrame
print(grouped_df)