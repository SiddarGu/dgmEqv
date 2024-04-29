
import matplotlib.pyplot as plt
import pandas as pd

# Create figure and axes
plt.figure(figsize=(8,6))
ax=plt.subplot()

# Create dataframe
data = {'Month': ["January","February","March","April","May","June","July","August"], 
        'Electricity Usage': [500,550,600,650,750,800,900,850],
        'Renewable Energy Usage': [400,450,400,500,550,600,700,750]
}
df = pd.DataFrame(data)

# Plot line chart
plt.plot(df['Month'], df['Electricity Usage'], color='blue', marker='o', label='Electricity Usage')
plt.plot(df['Month'], df['Renewable Energy Usage'], color='green', marker='o', label='Renewable Energy Usage')

# Customize chart
plt.title('Energy Usage in a Household in 2021', fontdict={'fontsize':20})
plt.xticks(df['Month'], rotation=45, ha='right')
ax.set_xlabel('Month')
ax.set_ylabel('Usage (kWh)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='-', color='gray')
plt.legend(loc='best')

# Save and clear state
plt.tight_layout()
plt.savefig('line chart/png/15.png')
plt.cla()