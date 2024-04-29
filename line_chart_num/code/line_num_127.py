
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK', 'Canada', 'Mexico', 'Germany']
volunteer_hours = [1000, 800, 1200, 900, 1100]
donations = [100, 60, 80, 50, 70]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

ax.plot(country, volunteer_hours, label='Volunteer Hours', color='green')
ax.plot(country, donations, label='Donations (million dollars)', color='red')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

for x, y in zip(country, volunteer_hours):
    ax.annotate('{0:,}'.format(y), (x, y), xytext=(0, -20), textcoords='offset points',
                va='top', ha='center', rotation=45, fontsize=9)

for x, y in zip(country, donations):
    ax.annotate('{0:,}'.format(y), (x, y), xytext=(0, 10), textcoords='offset points',
                va='bottom', ha='center', rotation=45, fontsize=9)

ax.set_title('Volunteer Hours and Donations to Nonprofit Organizations in Selected Countries', fontsize=14, wrap=True)
ax.set_xticks(country)
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('line chart/png/85.png')
plt.clf()