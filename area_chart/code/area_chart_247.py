
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data_dict = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 
             'Theater Visitors': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050], 
             'Concert Attendees': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150], 
             'Museum Visitors': [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250], 
             'Art Gallery Visitors': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]}

# Process data using pandas
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot data with area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Month'], df['Theater Visitors'], df['Concert Attendees'], df['Museum Visitors'], df['Art Gallery Visitors'], labels=['Theater Visitors', 'Concert Attendees', 'Museum Visitors', 'Art Gallery Visitors'], alpha=0.5)

# Set x and y axis ticks and labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_xticklabels(df['Month'], rotation=45, ha='right', rotation_mode='anchor')

# Set grid lines
ax.grid(True, color='lightgray', linestyle='dashed', axis='y')

# Set legend position and labels
ax.legend(loc='upper left')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Visitors')

# Set title
ax.set_title('Visitor Trends in Arts and Culture Venues by Month')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_94.png', bbox_inches='tight')

# Clear current image state
plt.clf()