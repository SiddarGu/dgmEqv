
import matplotlib.pyplot as plt
import numpy as np

# data
Year = [2000, 2005, 2010, 2015, 2020]
Health_Care_Spending = [3.5, 4.2, 4.7, 5.3, 6.0]
Average_Life_Expectancy = [75.8, 76.1, 76.5, 77.3, 78.1]

# create figure
plt.figure(figsize=(10, 8))

# draw line chart
plt.plot(Year, Health_Care_Spending, color='red', label='Health Care Spending(trillion dollars)')
plt.plot(Year, Average_Life_Expectancy, color='blue', label='Average Life Expectancy(years)')

# set x, y limit
plt.xlim(1999, 2021)
plt.ylim(75, 78.2)

# set x, y ticks
plt.xticks(Year)
plt.yticks(np.arange(75, 78.2, 0.2))

# set label
plt.xlabel('Year')
plt.ylabel('Value')

# set title
plt.title('Health Care Spending and Average Life Expectancy in the United States from 2000 to 2020')

# set legend
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')

# fit the figure
plt.tight_layout()

# save and show figure
plt.savefig('line chart/png/354.png')
plt.show()

# clear figure
plt.clf()