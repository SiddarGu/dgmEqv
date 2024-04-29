
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(12, 8))

# set axis and labels
plt.title('Comparison of Case Types in US Law Courts from 2001 to 2004')
plt.xlabel('Year')
plt.ylabel('Number of Cases')

# plot data
years = np.array([2001, 2002, 2003, 2004])
criminal_cases = np.array([13000, 14000, 16000, 18000])
civil_cases = np.array([24000, 26000, 25000, 28000])
business_cases = np.array([15000, 17000, 19000, 17000])
plt.plot(years, criminal_cases, label='Criminal Cases')
plt.plot(years, civil_cases, label='Civil Cases')
plt.plot(years, business_cases, label='Business Cases')

# set xticks
plt.xticks(years)

# add legend
plt.legend(loc='upper left')

# label each point
for x, y in zip(years, criminal_cases):
    plt.annotate(f'{y}', xy=(x, y), xytext=(x-0.2, y+500),
            fontsize=10, color='b')
for x, y in zip(years, civil_cases):
    plt.annotate(f'{y}', xy=(x, y), xytext=(x+0.2, y-500),
            fontsize=10, color='g')
for x, y in zip(years, business_cases):
    plt.annotate(f'{y}', xy=(x, y), xytext=(x, y+300),
            fontsize=10, color='r')

# add grid
plt.grid()

# resize figure
plt.tight_layout()

# save figure
plt.savefig('line chart/png/343.png')

# clear the figure
plt.clf()