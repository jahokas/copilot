# create a list lenght of 20 with random numbers between 1 and 6 and create a dataframe named df_analysis with the list as a column named 'customer_id'
import random
import pandas as pd
list1 = [random.randint(1, 6) for i in range(20)]
# change the type of the column 'customer_id' to string
list1 = [str(i) for i in list1]
df_analysis = pd.DataFrame({'customer_id': list1})
# add a new column in df_analysis that contains random string values in each row and random strings can have two values: 'accepted' or 'rejected'
# values 'accepted' or 'rejected' are fully random and not based on any condition
df_analysis['status'] = ['accepted' if random.randint(0, 1) == 0 else 'rejected' for i in range(20)]
# add a new column in df_analysis that contains random string dates in each row and random dates are between 01/01/2023 and 03/31/2023
import datetime as dt
start_date = dt.date(2023, 1, 1)
end_date = dt.date(2023, 3, 31)
date_list = [start_date + dt.timedelta(days=random.randint(0, 89)) for i in range(20)]
df_analysis['date'] = date_list
# change the type of the column 'date' to datetime
df_analysis['date'] = pd.to_datetime(df_analysis['date'])
# add a new column named month_year in df_analysis that is based on the values of the column 'date' and contains the month and year in the format MM-YYYY
df_analysis['month_year'] = df_analysis['date'].dt.strftime('%Y-%m')
# sort the dataframe first by column 'date' in ascending order and then by column 'customer_id' in descending order
df_analysis = df_analysis.sort_values(by=['customer_id', 'date'], ascending=[True, False])
# reindex the dataframe
df_analysis = df_analysis.reset_index(drop=True)
print('first dataframe')
print(df_analysis)
# group the dataframe by column 'customer_id' and 'month_year' and leave only the first row of each group in the dataframe
df_analysis = df_analysis.groupby(['customer_id', 'month_year']).first().reset_index()
print('second dataframe')
# print the dataframe
print(df_analysis)