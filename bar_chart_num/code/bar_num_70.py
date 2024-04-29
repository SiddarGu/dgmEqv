
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

x_values = [2019,2020,2021]
revenue = [500,550,600]
profits = [100,90,110]
assets = [2000,2200,2400]

ax.bar(x_values,revenue,label='Revenue',bottom=profits)
ax.bar(x_values,profits,label='Profits',bottom=assets)
ax.bar(x_values,assets,label='Assets')

ax.set_title('Financial performance of a company from 2019 to 2021')
ax.set_xlabel('Year')

ax.set_xticks([2019,2020,2021])
ax.set_xticklabels(['2019','2020','2021'], fontsize=12, rotation=20)
ax.legend(loc='best')

for x,y in zip(x_values,revenue):
    ax.annotate('{}'.format(y), xy=(x,y/2), va='center', ha='center', fontsize=15, color='white')

for x,y in zip(x_values,profits):
    ax.annotate('{}'.format(y), xy=(x,y/2+y+assets[x-2019]), va='center', ha='center', fontsize=15, color='white')

for x,y in zip(x_values,assets):
    ax.annotate('{}'.format(y), xy=(x,y/2+y), va='center', ha='center', fontsize=15, color='white')

plt.tight_layout()
plt.savefig('Bar Chart/png/468.png')
plt.clf()