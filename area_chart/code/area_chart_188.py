
#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#set data as dictionary
data = {'Category': ['Agriculture', 'Manufacturing', 'Transportation', 'Residential', 'Commercial', 'Waste Management', 'Renewable Energy', 'Mining', 'Technology', 'Retail', 'Healthcare', 'Education', 'Government', 'Tourism'],
        'Carbon Emissions (kg)': [200, 300, 400, 250, 350, 200, 300, 350, 400, 250, 300, 200, 400, 350],
        'Water Usage (liters)': [500, 400, 300, 350, 250, 200, 350, 300, 400, 350, 250, 300, 300, 350],
        'Waste Produced (kg)': [350, 250, 200, 400, 300, 200, 300, 200, 300, 300, 200, 250, 300, 400],
        'Energy Consumption (kWh)': [300, 350, 400, 200, 250, 150, 200, 250, 300, 200, 300, 200, 300, 250]}

#convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#set figure size
fig, ax = plt.subplots(figsize=(12, 8))

#calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

#plot area chart
ax.stackplot(df['Category'], df['Carbon Emissions (kg)'], df['Water Usage (liters)'], df['Waste Produced (kg)'], df['Energy Consumption (kWh)'], labels=['Carbon Emissions (kg)', 'Water Usage (liters)', 'Waste Produced (kg)', 'Energy Consumption (kWh)'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

#set ticks and ticklabels for x axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

#set grid lines
ax.grid(linestyle='--')

#set title
plt.title('Environmental Impact by Industry Category')

#set legend
leg = ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

#set legend's title
leg.set_title('Unit', prop={'size': 12})

#resize image
fig.tight_layout()

#save image
fig.savefig('output/final/area_chart/png/20231228-145339_2.png', bbox_inches='tight')

#clear current image state
plt.clf()