
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define and process the data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Psychology (Publications)': [100, 120, 150, 180, 200],
        'Sociology (Publications)': [120, 140, 160, 170, 180],
        'Anthropology (Publications)': [150, 130, 180, 200, 170],
        'History (Publications)': [200, 180, 150, 120, 100],
        'Political Science (Publications)': [100, 120, 150, 180, 200]}

df = pd.DataFrame(data)  # Create a dataframe 
df.iloc[:, 0] = df.iloc[:, 0].astype(str)  # Convert first column to string type

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data as an area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.7)

# Set x and y axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)

# Calculate the max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    yticks = np.linspace(0, max_total_value, 3, dtype=np.int32)
elif max_total_value > 10 and max_total_value <= 100:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
elif max_total_value > 100 and max_total_value <= 1000:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
else:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set tick labels and rotate if necessary
if len(str(max_total_value)) > 6:
    ax.tick_params(axis='y', rotation=45, ha='right', rotation_mode='anchor')
    ax.set_yticklabels([str(tick) for tick in yticks], wrap=True)
else:
    ax.set_yticklabels([str(tick) for tick in yticks])

# Set grid lines
ax.grid(axis='y', linestyle='--')

# Set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

# Set title and labels
ax.set_title('Publications in Social Sciences and Humanities from 2015 to 2019')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_63.png', bbox_inches='tight')

# Clear the current image state
plt.clf()