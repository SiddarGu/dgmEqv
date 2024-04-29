

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,5))
ax = plt.subplot()

# Data
Year = np.array([2017,2018,2019,2020,2021,2022])
Number_of_Visitors = np.array([80,85,90,80,95,100])
Revenue = np.array([150,170,185,160,190,200])

# Plotting
ax.plot(Year, Number_of_Visitors, '-o', c='b', label='Number of Visitors (millions)')
ax.plot(Year, Revenue, '-o', c='r', label='Revenue (billion dollars)')

# Add labels
for i, txt in enumerate(Number_of_Visitors):
    ax.annotate(txt, (Year[i], Number_of_Visitors[i]), rotation=90)

for i, txt in enumerate(Revenue):
    ax.annotate(txt, (Year[i], Revenue[i]), rotation=90)

# Set Labels
ax.set_title('Tourist Visits and Revenue Generated in the Last Six Years', fontsize=15, fontweight='bold')
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Value', fontsize=13)
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)

# Formatting
plt.xticks(Year, fontsize=10)
plt.tight_layout()
plt.savefig('line chart/png/275.png')

plt.clf()