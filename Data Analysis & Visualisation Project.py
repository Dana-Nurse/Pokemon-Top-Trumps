#Project Brief: Data Analysis & Visualisation Spreadsheet
import pandas as pd
# Read data from a CSV file
csv_file_path = 'D:\Python\sales.csv'
csv_data = pd.read_csv(csv_file_path)
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
# Display the entire DataFrame
print(csv_data)


# Open and read a text file
file_path = 'D:\Python\sales.csv'

# Open the file in read mode
with open(file_path, 'r') as file:
    file_contents = file.read()
    print(file_contents)


import csv
def monthlySales():
    with open('D:\Python\sales.csv', 'r') as sales_file:  #calls and read data from the sales.csv file.
        spreadsheet = csv.DictReader(sales_file)
        for row in spreadsheet:
            print(row['month'])
            print(row['sales'])
monthlySales()  # calling the our defined function



# Calculate the total sales
total_sales = csv_data['sales'].sum()
print("Total Sales: £{:,.2f}".format(total_sales))

# explain the yearly changes as a percentage

import pandas as pd
import csv

# Read data from CSV file and define file path
csv_file_path = 'D:\Python\project.csv'  # Replace with your CSV file path
csv_data = pd.read_csv(csv_file_path)

# Display all data from the file
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
# Display the entire DataFrame
print(csv_data)


# Filter for data in the "all" row
all_sector_data = csv_data[csv_data['LCREE SECTORS'] == 'All']

# Calculate yearly percentage changes
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
percentage_changes = []

for year_index in range(len(years) - 1):
    initial_value = all_sector_data[years[year_index]].iloc[0]
    final_value = all_sector_data[years[year_index + 1]].iloc[0]

    yearly_percentage_change = ((final_value - initial_value) / initial_value) * 100
    percentage_changes.append(yearly_percentage_change)

# Print the yearly percentage changes to 2 decimal points
for year_index, year in enumerate(years[1:]):
    print(f"Year {year}: {percentage_changes[year_index]:.2f}%")


#find the average of All Sectors
import locale
import pandas as pd

# Set the locale to display numbers with thousands separator and currency symbol
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

file_path = 'D:\Python\project.csv'
df = pd.read_csv(file_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, index_col=0)

sector_name = 'All'

# Calculate the average for the specified sector
average_for_sector = df.loc[sector_name].mean()

#format with two decimal places
formatted_average = locale.format_string('%.2f', average_for_sector , grouping=True)

# Add the currency symbol (£)
formatted_average = '£' + formatted_average

print(f"Average for {sector_name}: {formatted_average}")

# Python program to illustrate
# Plotting categorical scatter
# plots with Seaborn

# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns

# x axis values
x =['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# y axis values
y =[19910000,20933500,19480500,20088000,22259000,27286500, 23850000, 28616000]

# Create a DataFrame
data = {'Years': x, 'LCREE SECTORS': y}
df = pd.DataFrame(data)

# Set the plotting style
sns.set(style="whitegrid")

# plotting strip plot with seaborn
ax = sns.stripplot(x='Years', y='LCREE SECTORS', data=df)

# giving labels to x-axis and y-axis
ax.set(xlabel='Years', ylabel='LCREE SECTORS')

# giving title to the plot
plt.title('LCREE SECTORS between the periods of 2014-2021')

# function to show plot
plt.show()
#########################################
#Find the highest and lowest

import locale
import pandas as pd
# Read the CSV file into a DataFrame
file_path = 'D:\Python\project.csv'
df = pd.read_csv(file_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, index_col=0)

sector_name = 'All'

# Find the highest and lowest sales values
highest_sales = df.loc['All'].max()
lowest_sales = df.loc['All'].min()

# Print the results
print(f"Highest sales:£{highest_sales:,.2f}")
print(f"Lowest sales:£{lowest_sales:,.2f}")
##########################################################
#final
import locale

# Set the locale to display numbers with thousands separator and currency symbol
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

import pandas as pd

# Specify the file path to the CSV file
file_path = 'D:\Python\project.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# To access specific rows or columns, you can use DataFrame indexing and slicing
all_sector_data = df.loc[df['LCREE SECTORS'] == 'All', '2014':'2021']


# To calculate the highest and lowest turnover for the 'All' row, you can use:
highest_turnover_year = all_sector_data.idxmax(axis=1).values[0]
highest_turnover_value = all_sector_data.max(axis=1).values[0]
lowest_turnover_year = all_sector_data.idxmin(axis=1).values[0]
lowest_turnover_value = all_sector_data.min(axis=1).values[0]

print(f"Highest turnover: £{highest_turnover_value:,.2f} in {highest_turnover_year}")
print(f"Lowest turnover:  £{lowest_turnover_value:,.2f} in {lowest_turnover_year}")