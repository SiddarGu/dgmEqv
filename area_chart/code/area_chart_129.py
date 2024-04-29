
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent the data using a dictionary
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Healthcare Spending ($)': [4000, 4200, 4500, 4700, 5000, 5300, 5500, 5800, 6000],
    'Education Spending ($)': [3500, 3800, 4000, 4200, 4500, 4800, 5000, 5300, 5500],
    'Infrastructure Spending ($)': [3000, 3200, 3500, 3700, 4000, 4300, 4500, 4800, 5000],
    'Social Welfare Spending ($)': [2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart
fig, ax = plt.subplots(figsize=(12, 8)) # Set the figsize parameter to a larger setting to prevent content from being displayed
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.7)
ax.legend(loc='upper left') # Adjust the legend's position appropriately to avoid overlapping with the content
ax.set_title('Government Spending by Category from 2015 to 2023') # Set the title of the figure
ax.grid(linestyle='dotted') # Set background grid lines
ax.set_xlabel('Year', ha='right', rotation_mode='anchor', rotation=45) # If the text length of the x ticks' label more than 6 characters, use the method of adding the parameter "rotation" or separate lines by setting "wrap=true"
ax.set_ylabel('Spending ($)', ha='right', rotation_mode='anchor', rotation=0) # If the text length of the y ticks' label more than 6 characters, use the method of adding the parameter "rotation" or separate lines by setting "wrap=true"
ax.set_xlim(0, len(df.index) - 1) # Set the x axis range
max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate the max total value
max_total_value = np.ceil(max_total_value / 100) * 100 # Ceil max_total_value up to the nearest multiple of 100
ax.set_ylim(0, max_total_value) # Set the y axis range
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticks and ticklabels
fig.tight_layout() # Automatically resize the image by tight_layout() before savefig()
fig.savefig('output/final/area_chart/png/20231228-140159_43.png', bbox_inches='tight') # Save the figure with the parameter "bbox_inches='tight'"
plt.close(fig) # Clear the current image state