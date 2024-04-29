import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Hospital Bed Occupancy (%)': ["60-70", "70-80", "80-90", "90-100"],
    'Number of Hospitals': [8, 17, 23, 5]
}

# Converting to variables
data_labels = ['Hospital Bed Occupancy (%)', 'Number of Hospitals']
line_labels = data['Hospital Bed Occupancy (%)']
data_values = data['Number of Hospitals']

# Creating a DataFrame from the dictionary
df = pd.DataFrame(data, columns=data_labels)

# Setting the figure size to be larger and adding a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Creating a vertical histogram
df.plot(kind='bar', x='Hospital Bed Occupancy (%)', y='Number of Hospitals', ax=ax, rot=0, color='skyblue', grid=True)

# Setting the title
ax.set_title('Hospital Bed Occupancy Rates Across Multiple Hospitals')

# Handling long text
ax.set_xticklabels(df['Hospital Bed Occupancy (%)'], rotation=45, ha='right')

# Automatically adjusting parameter to prevent content from being displayed improperly
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/131.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
