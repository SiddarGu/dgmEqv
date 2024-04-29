
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Year': [2016, 2017, 2018, 2019, 2020], 
        'Anthropology (Graduates)': [120, 130, 140, 150, 160],
        'Psychology (Graduates)': [150, 160, 170, 180, 190],
        'Sociology (Graduates)': [130, 140, 150, 160, 170],
        'Political Science (Graduates)': [100, 120, 130, 140, 150],
        'Education (Graduates)': [200, 210, 220, 230, 240]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100)*100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data with area chart
ax.stackplot(df['Year'], df['Anthropology (Graduates)'], df['Psychology (Graduates)'], df['Sociology (Graduates)'], df['Political Science (Graduates)'], df['Education (Graduates)'], labels=['Anthropology', 'Psychology', 'Sociology', 'Political Science', 'Education'])

# Add grid lines
ax.grid(axis='both', linestyle='--', alpha=0.5)

# Set legend and title
ax.legend(loc='upper left')
ax.set_title('Graduates in Social Sciences and Humanities from 2016 to 2020')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_76.png', bbox_inches='tight')

# Clear image state
plt.clf()