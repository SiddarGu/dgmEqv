

import matplotlib.pyplot as plt
import pandas as pd
 
# Create dataframe
df = pd.DataFrame({'Month':['January','February','March','April'], 
                   'Crop A':[1000,1200,800,1500], 
                   'Crop B':[800,900,1100,1200], 
                   'Crop C':[1200,1100,1300,1400],
                   'Crop D':[1500,1600,1200,800]})
 
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
 
# Plot line chart
ax.plot(df['Month'], df['Crop A'], marker='o', markersize=10, label='Crop A')
ax.plot(df['Month'], df['Crop B'], marker='d', markersize=10, label='Crop B')
ax.plot(df['Month'], df['Crop C'], marker='s', markersize=10, label='Crop C')
ax.plot(df['Month'], df['Crop D'], marker='*', markersize=10, label='Crop D')
 
# Set x, y axis label
ax.set_title('Crop Production in four categories in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Production (tonnes)')
 
# Display label of each data point
for i, txt in enumerate(df['Crop A']):
    ax.annotate(txt, (df['Month'][i], df['Crop A'][i]), rotation=45)
for i, txt in enumerate(df['Crop B']):
    ax.annotate(txt, (df['Month'][i], df['Crop B'][i]), rotation=45)
for i, txt in enumerate(df['Crop C']):
    ax.annotate(txt, (df['Month'][i], df['Crop C'][i]), rotation=45)
for i, txt in enumerate(df['Crop D']):
    ax.annotate(txt, (df['Month'][i], df['Crop D'][i]), rotation=45)
 
# Set legend
ax.legend(loc='best', fontsize='large')
 
# Set x-axis tick
plt.xticks(df['Month'])
 
# Display grid
plt.grid(axis='y', linestyle='-.')
 
# Resize image
plt.tight_layout()
 
# Save image
plt.savefig('line chart/png/594.png')
 
# Clear image state
plt.clf()