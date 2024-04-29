
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = [['January', 75, 2.4, 0.6], 
        ['February', 80, 2.8, 0.7], 
        ['March', 90, 3.2, 0.8],
        ['April', 85, 2.7, 0.7],
        ['May', 83, 2.6, 0.7],
        ['June', 80, 2.5, 0.7],
        ['July', 77, 2.4, 0.6],
        ['August', 76, 2.3, 0.6]]

df = pd.DataFrame(data, columns=['Month', 'Average Speed(km/hr)', 'Fuel Consumption(litres/100km)', 'Emissions(tonnes)'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.plot(df['Month'], df['Average Speed(km/hr)'], 'b-', label='Average Speed(km/hr)')
ax.plot(df['Month'], df['Fuel Consumption(litres/100km)'], 'r-', label='Fuel Consumption(litres/100km)')
ax.plot(df['Month'], df['Emissions(tonnes)'], 'g-', label='Emissions(tonnes)')

ax.set_title('Average speed, fuel consumption and emissions of a vehicle in a year')
ax.set_xlabel('Month')
ax.set_ylabel('Quantity')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True)
ax.xaxis.set_ticks(np.arange(len(df['Month'])))
ax.xaxis.set_ticklabels(df['Month'], rotation=45, ha="right", wrap=True)

for i in range(len(df['Month'])):
    ax.annotate(str(df['Average Speed(km/hr)'][i]), xy=(i, df['Average Speed(km/hr)'][i]), 
                xytext=(2, 10), textcoords='offset points', fontsize=12)
    ax.annotate(str(df['Fuel Consumption(litres/100km)'][i]), xy=(i, df['Fuel Consumption(litres/100km)'][i]), 
                xytext=(2, 10), textcoords='offset points', fontsize=12)
    ax.annotate(str(df['Emissions(tonnes)'][i]), xy=(i, df['Emissions(tonnes)'][i]), 
                xytext=(2, 10), textcoords='offset points', fontsize=12)

plt.tight_layout()
plt.savefig('line chart/png/41.png')
plt.clf()