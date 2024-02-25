# create two lists lenght of 10 with random numbers between 1 and 10 and create a dataframe named df_randoms
import random
import pandas as pd
list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]
df_randoms = pd.DataFrame({'A': list1, 'B': list2})
# create a new column in df_randoms that is the sum of the two columns
df_randoms['C'] = df_randoms['A'] + df_randoms['B']
# create a new column in df_randoms that contains random string values in each row and random strings can have two values: 'even' or 'odd'
df_randoms['D'] = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
# create a new column in df_randoms that contains random string values in each row and random strings can have two values: 'accepted' or 'rejected'
# values 'accepted' or 'rejected' are fully random and not based on any condition
df_randoms['E'] = ['accepted' if random.randint(0, 1) == 0 else 'rejected' for i in range(10)]
# create a new column in df_randoms that contains random string dates in each row and random dates are between 01/01/2023 and 12/31/2023
# import the datetime module
import datetime as dt
# create a new column in df_randoms that contains random string dates in each row and random dates are between 01/01/2023 and 12/31/2023
start_date = dt.date(2023, 1, 1)
end_date = dt.date(2023, 12, 31)
date_list = [start_date + dt.timedelta(days=random.randint(0, 364)) for i in range(10)]
df_randoms['Dates'] = date_list
# remove the columns 'A' and 'B' and 'C' and 'D' from the dataframe
df_randoms = df_randoms.drop(columns=['A', 'B', 'C', 'D']) 
# sort the dataframe first by column 'D' in ascending order and then by column 'Dates' in descending order
df_randoms = df_randoms.sort_values(by=['E', 'Dates'], ascending=[True, False])
# print the dataframe
print(df_randoms)



