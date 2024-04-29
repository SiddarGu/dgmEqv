
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
GDP = [21300,2900,3400,2700]
Growth_Rate = [3.2,2.3,2.5,2.7]
Inflation_Rate = [1.7,1.2,1.5,1.4]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.bar(Country, GDP, bottom=np.array(Growth_Rate)+np.array(Inflation_Rate), label='GDP', color='blue')
ax.bar(Country, Growth_Rate, bottom=Inflation_Rate, label='GDP Growth Rate', color='orange')
ax.bar(Country, Inflation_Rate, label='Inflation Rate', color='green')

ax.set_title('GDP, Growth Rate and Inflation Rate of Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Amount')

ax.legend()

pos = np.arange(len(Country))
for i, v in enumerate(GDP):
    ax.text(pos[i]-0.15, v/2+np.array(Growth_Rate)[i]+np.array(Inflation_Rate)[i], str(v)+'B', fontsize=10, color='white')
for i, v in enumerate(Growth_Rate):
    ax.text(pos[i]-0.15, v/2+np.array(Inflation_Rate)[i], str(v)+'%', fontsize=10, color='white')
for i, v in enumerate(Inflation_Rate):
    ax.text(pos[i]-0.15, v/2, str(v)+'%', fontsize=10, color='white')

ax.set_xticks(pos)
ax.set_xticklabels(Country, rotation=45, ha='right')

plt.tight_layout()

plt.savefig('Bar Chart/png/3.png', dpi=300)
plt.clf()