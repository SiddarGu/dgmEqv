
import matplotlib.pyplot as plt
import numpy as np

# create figure and plot data
plt.figure(figsize=(12,7))
plt.plot(np.arange(2018, 2022), [300000, 350000, 400000, 450000], label='Average Home Price (dollars)')
plt.plot(np.arange(2018, 2022), [1500, 1600, 1700, 1800], label='Average Rent Price (dollars)')
plt.plot(np.arange(2018, 2022), [2, 3, 4, 5], label='Vacancy Rate')

# add legend, title, ticks
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Changes in Home Prices, Average Rent Prices, and Vacancy Rates in the US from 2018 to 2021')
plt.xticks(np.arange(2018, 2022))

# adjust the figure size
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/207.png', bbox_inches='tight')

# clear the figure state
plt.clf()