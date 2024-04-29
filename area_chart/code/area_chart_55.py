
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Year': [2016, 2017, 2018, 2019, 2020], 
        'Concerts (Attendees)': [10000, 12000, 13000, 15000, 11000], 
        'Sports Events (Attendees)': [15000, 17000, 19000, 20000, 18000], 
        'Movie Premieres (Attendees)': [12000, 14000, 15000, 16000, 13000], 
        'Festivals (Attendees)': [8000, 9000, 10000, 11000, 9000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Plot the data with an area chart
ax = fig.add_subplot(111)
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], 
             labels=['Concerts', 'Sports Events', 'Movie Premieres', 'Festivals'], 
             colors=['#FACF7A', '#7AB6F5', '#75D3B1', '#F5A17A'], alpha=0.7)

# Set x and y axis ticks and labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)
ax.set_xticks(np.arange(len(df.iloc[:, 0])))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(np.linspace(0, ax.get_ylim()[1], np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Number of Attendees')

# Add background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend position and remove overlapping with content
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

# Automatically resize image
plt.tight_layout()

# Add title
plt.title('Attendance Trends for Popular Events from 2016 to 2020')

# Save the image
plt.savefig('output/final/area_chart/png/20231228-131755_31.png', bbox_inches='tight')

# Clear the current image state
plt.clf()