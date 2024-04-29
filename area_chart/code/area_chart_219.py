
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Convert data to dictionary
data = {'Year': [2015, 2016, 2017, 2018, 2019], 
        'Coursework (Hours)': [200, 180, 220, 210, 250], 
        'Study Time (Hours)': [50, 60, 70, 80, 90], 
        'Extra Curricular (Hours)': [100, 120, 90, 110, 100], 
        'Research (Hours)': [150, 140, 130, 120, 110], 
        'Internship (Hours)': [50, 60, 70, 80, 90]}

# Convert data to dataframe
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Set x and y axis ticks and ticklabels
ax = plt.subplot()
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index)-1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    
# Set background grid lines
ax.grid(linestyle='dotted', alpha=0.3)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Set y axis limit and ticks
if max_total_value <= 10:
    ax.set_ylim(0, 10)
    ax.set_yticks(np.arange(0, 10, 1))
elif max_total_value <= 100:
    ax.set_ylim(0, np.ceil(max_total_value/10)*10)
    ax.set_yticks(np.arange(0, np.ceil(max_total_value/10)*10, 10))
elif max_total_value <= 1000:
    ax.set_ylim(0, np.ceil(max_total_value/100)*100)
    ax.set_yticks(np.arange(0, np.ceil(max_total_value/100)*100, 100))
else:
    ax.set_ylim(0, np.ceil(max_total_value/1000)*1000)
    ax.set_yticks(np.arange(0, np.ceil(max_total_value/1000)*1000, 1000))

# Plot the data with stackplot
ax.stackplot(df['Year'], df['Coursework (Hours)'], df['Study Time (Hours)'], df['Extra Curricular (Hours)'], df['Research (Hours)'], df['Internship (Hours)'], labels=['Coursework', 'Study Time', 'Extra Curricular', 'Research', 'Internship'], alpha=0.7)

# Set legend position and size
ax.legend(loc='upper left', fontsize='medium')

# Set title
ax.set_title('Distribution of Time Spent on Education and Academics')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_62.png', bbox_inches='tight')

# Clear current image state
plt.clf()