
import matplotlib.pyplot as plt
import numpy as np

region = ['North America','Europe','Asia','Africa']
Electricity_Consumption = [1000, 900, 1100, 800] 
Renewable_Energy = [800, 700, 900, 600]

x = np.arange(len(region))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, Electricity_Consumption, width, label='Electricity Consumption(kwh)')
rects2 = ax.bar(x + width/2, Renewable_Energy, width, label='Renewable Energy(kwh)')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('kwh')
ax.set_title('Electricity consumption and renewable energy usage in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.legend(loc=2)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=45, wrap=True)

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.savefig('Bar Chart/png/219.png')
plt.clf()