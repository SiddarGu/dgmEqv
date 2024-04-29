
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
GDP = [21000,3000,4000,3500]
GDP_Growth_Rate = [3.5,2.2,1.8,2.1]
Unemployment_Rate = [5.9,4.4,5.2,7.9]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

bar1 = ax.bar(country, GDP, label='GDP(billion)')

for bar in bar1:
    yval = bar.get_height()
    ax.annotate('{:.0f}'.format(yval),xy=(bar.get_x() + bar.get_width()/2, yval), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

bar2 = ax.bar(country, GDP_Growth_Rate, bottom=GDP, label='GDP Growth Rate')

for bar in bar2:
    yval = bar.get_height()
    ax.annotate('{:.1f}%'.format(yval),xy=(bar.get_x() + bar.get_width()/2, yval+sum(GDP)), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

bar3 = ax.bar(country, Unemployment_Rate, bottom=[i+j for i,j in zip(GDP, GDP_Growth_Rate)], label='Unemployment Rate')

for bar in bar3:
    yval = bar.get_height()
    ax.annotate('{:.1f}%'.format(yval),xy=(bar.get_x() + bar.get_width()/2, yval+sum([i+j for i,j in zip(GDP, GDP_Growth_Rate)])), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
    
ax.set_xticks(country)
ax.set_title('GDP, growth rate and unemployment rate in four countries in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/418.png')
plt.clf()