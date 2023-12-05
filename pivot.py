import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022],
    'City': ['City1', 'City2', 'City1', 'City2', 'City1', 'City2', 'City1', 'City2'],
    'Product': ['Coffee', 'Coffee', 'Tea', 'Tea', 'Coffee', 'Coffee', 'Sugar', 'Sugar'],
    'Sales': [100, 150, 80, 120, 120, 180, 50, 70]
}

df = pd.DataFrame(data)

# Creating a pivot table
pivot_table = pd.pivot_table(df, values='Sales', index=['Year', 'City'], columns='Product', aggfunc='sum', fill_value=0, margins=True, margins_name='Total')

# Displaying the desired format
desired_columns = ['Coffee', 'Sugar', 'Tea', 'Total']
pivot_table = pivot_table[desired_columns]
print(pivot_table)

# Visualization for City1 - Line chart for each product
city1_data = df[df['City'] == 'City1']
pivot_table_city1 = pd.pivot_table(city1_data, values='Sales', index='Year', columns='Product', aggfunc='sum', fill_value=0)
pivot_table_city1.plot(kind='line', marker='o')
plt.title('Yearly Sales of Products in City1')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend(title='Product', loc='upper left')
plt.show()
