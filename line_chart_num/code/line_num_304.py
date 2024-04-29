
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(8, 6))

# read data 
year = [2020, 2021, 2022, 2023, 2024]
average_price_per_lb_USD = [2.5, 2.7, 2.8, 2.9, 3.1]
average_consumption_lbs = [20, 22, 24, 26, 28]

# add subplot
ax = fig.add_subplot()

# plot line chart
ax.plot(year, average_price_per_lb_USD, '-o', color = 'blue', label = 'Average Price per lb (USD)')
ax.plot(year, average_consumption_lbs, '-o', color = 'orange', label = 'Average Consumption (lbs)')

# add xticks 
ax.set_xticks(year)

# add title and labels 
ax.set_title('Average price and consumption of beef in the United States from 2020 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Average Price per lb (USD) / Average Consumption (lbs)')

# add legend
ax.legend(loc='upper left')

# annotate  
for i,j in zip(year, average_price_per_lb_USD):
    ax.annotate(f'{j:.1f}',xy=(i,j),ha='center')

for i,j in zip(year, average_consumption_lbs):
    ax.annotate(f'{j:.0f}',xy=(i,j),ha='center')

# adjust the layout
plt.tight_layout()

# save fig
plt.savefig('line chart/png/227.png')

# clear the figure
plt.clf()