
import matplotlib.pyplot as plt
import pandas as pd

# Define data 
data = {'Year': [2020, 2021, 2022, 2023],
        'Electricity (MWh)': [30000, 32000, 34000, 36000],
        'Gas (MMcf)': [400, 450, 500, 550],
        'Oil (bbl)': [25000, 26000, 27000, 28000]}

# Read data into a Pandas DataFrame
df = pd.DataFrame(data)

# Define the width of the bars
barWidth = 0.2

# Set up the plot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot the bars
ax.bar(df['Year']-barWidth, df['Electricity (MWh)'], width=barWidth, label='Electricity', color='#FFC222')
ax.bar(df['Year'], df['Gas (MMcf)'], width=barWidth, label='Gas', color='#EE82EE')
ax.bar(df['Year']+barWidth, df['Oil (bbl)'], width=barWidth, label='Oil', color='#1E90FF')

# Set up properties of the plot
ax.set_ylabel('Amount (MWh, MMcf, bbl)')
ax.set_xlabel('Year')
ax.set_title('Energy production in three categories from 2020 to 2023')
ax.set_xticks(df['Year'])
ax.set_xticklabels(df['Year'], rotation=90, ha='center')
ax.legend(loc='best', bbox_to_anchor=(1, 0.5))
ax.grid()

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/504.png')

# Clear the current image state
plt.clf()