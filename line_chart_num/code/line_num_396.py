
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

# Create figure
fig = plt.figure(figsize=(10,5))

# Read data
data = [[2019,1000,800,400], [2020,1200,900,500], [2021,800,1100,600], [2022,1500,1200,700]]
df = pd.DataFrame(data, columns=['Year', 'Gross Profit','Net Income','Expenses'])

# Plot line chart
plt.plot(df['Year'], df['Gross Profit'], linestyle='-', marker='o', label='Gross Profit')
plt.plot(df['Year'], df['Net Income'], linestyle='-', marker='x', label='Net Income')
plt.plot(df['Year'], df['Expenses'], linestyle='-', marker='*', label='Expenses')

# Set title
plt.title('The Change of Gross Profit, Net Income, and Expenses of Business in 2019-2022')

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Amount (billion dollars)')
plt.legend(loc='upper left')

# Label data points
for a,b in zip(df['Year'], df['Gross Profit']):
    plt.annotate(str(b),xy=(a,b))

for a,b in zip(df['Year'], df['Net Income']):
    plt.annotate(str(b),xy=(a,b))

for a,b in zip(df['Year'], df['Expenses']):
    plt.annotate(str(b),xy=(a,b))

# Set ticks
plt.xticks(df['Year'])

# Resize and save
plt.tight_layout()
plt.savefig('line chart/png/125.png')

# Clear current image state
plt.clf()