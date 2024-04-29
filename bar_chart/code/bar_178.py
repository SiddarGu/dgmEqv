

import matplotlib.pyplot as plt
import numpy as np

# create figure
plt.figure(figsize=(8, 5))

# data
country = ['USA','UK','Germany','France']
GDP = [21,14.5,4.7,2.9]
unemployment_rate = [3.5,4,5,6.5]

# plot bar chart 
plt.bar(country, GDP, label='GDP (billion)', bottom=0, width=0.6, align='center', alpha=0.7)
plt.bar(country, unemployment_rate, label='Unemployment Rate', bottom=GDP, width=0.6, align='center', alpha=0.7)

# set titles, labels, ticks
plt.title('GDP and unemployment rate in four countries in 2021', fontsize=13, fontweight='bold', color='black')
plt.xlabel('Country')
plt.ylabel('Amount')
plt.xticks(country)

# legend
plt.legend(bbox_to_anchor=(1, 1), loc='upper right', ncol=1)

# grid
plt.grid(axis='y', alpha=0.5)

# resize
plt.tight_layout()

# save
plt.savefig('bar chart/png/401.png', bbox_inches='tight')

# clear
plt.clf()