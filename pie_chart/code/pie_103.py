
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
energy_df = pd.DataFrame({'Types of Energy': ['Solar','Wind','Hydroelectric','Nuclear','Natural Gas','Biomass'],
                         'Percentage': [25,20,20,15,10,10]})

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Plot pie chart
pie_chart = ax.pie(energy_df['Percentage'], labels=energy_df['Types of Energy'],
                  autopct='%.2f%%', shadow=True, explode=[0,0.1,0,0,0,0])

# Add legend
ax.legend(pie_chart[0], energy_df['Types of Energy'], bbox_to_anchor=(1.2,0.8),
          fontsize=10, loc="upper left")

# Add title
plt.title('Distribution of Renewable Energy Sources in the USA, 2023')

# Resize figure
plt.tight_layout()

# Save figure
fig.savefig('pie chart/png/171.png')

# Clear current image state
plt.clf()