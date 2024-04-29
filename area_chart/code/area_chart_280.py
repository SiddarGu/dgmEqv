
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent the data using a dictionary
data = {'Year':['2016','2017','2018','2019','2020'],
       'Math (Students)':[500,480,520,490,510],
       'Science (Students)':[400,420,380,420,400],
       'English (Students)':[600,550,580,540,560],
       'History (Students)':[300,320,280,310,320],
       'Art (Students)':[200,180,220,190,200]}

# Use pandas to process the data
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10,8))

# Set axis and plot the chart
ax = fig.add_subplot(111)
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#87CEEB','#FFDAB9','#FFA07A','#90EE90','#FFB6C1'], alpha=0.7)

# Set title
plt.title('Student Enrollment by Subject from 2016 to 2020')

# Set x axis label
ax.set_xlabel('Year')

# Set y axis label and unit
ax.set_ylabel('Number of Students')

# Set x axis tick labels
ax.set_xticklabels(df.iloc[:, 0])

# Set y axis tick labels
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set axis limit
ax.set_xlim(0, len(df.index) - 1)

# Set legend position
ax.legend(loc='upper left')

# Set background grid lines
ax.grid(color='grey', linestyle=':', linewidth=1, alpha=0.5)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_49.png', bbox_inches='tight')

# Clear the current image state
plt.clf()