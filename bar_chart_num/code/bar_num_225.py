
import matplotlib.pyplot as plt
import numpy as np

#data
country = ['USA', 'UK', 'Germany', 'France']
manufacturing_index = [90, 95, 80, 85]
industrial_production = [3.2, 4.7, 2.1, 3.5]
unemployment_rate = [6.2, 4.3, 5.4, 7.9]

# create figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

# draw bar chart
ax.bar(country, manufacturing_index, label='Manufacturing Index', color='green', bottom=industrial_production, hatch='/')
ax.bar(country, industrial_production, label='Industrial Production', color='blue', bottom=unemployment_rate, hatch='*')
ax.bar(country, unemployment_rate, label='Unemployment Rate', color='red', hatch='+')

# customize
ax.set_title('Manufacturing and Production Statistics for Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_xticks(country)
ax.set_ylabel('Index (%)')
ax.legend(loc='upper right')

# draw value on each bar
for index, value in enumerate(manufacturing_index):
    ax.annotate(str(value)+'%', xy=(index-0.2, value+unemployment_rate[index]), color='white')
for index, value in enumerate(industrial_production):
    ax.annotate(str(value)+'%', xy=(index-0.2, value+unemployment_rate[index]+manufacturing_index[index]), color='white')
for index, value in enumerate(unemployment_rate):
    ax.annotate(str(value)+'%', xy=(index-0.2, value), color='white')

# adjust size
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/77.png')

# clear state
plt.clf()