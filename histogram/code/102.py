import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = {
    'Crop Production (million metric tons)': ['Wheat', 'Rice', 'Corn', 'Soybeans', 'Potatoes', 'Tomatoes', 'Cabbage', 'Carrots'],
    'Number of Countries': [184.0, 166.2, 180.5, 131.3, 70.1, 48.5, 45.2, 37.7]
}

# Transforming data into DataFrame
df = pd.DataFrame(data)

# Labels
data_labels = ['Number of Countries']
line_labels = df['Crop Production (million metric tons)']

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
df.plot(kind='barh', x='Crop Production (million metric tons)', y='Number of Countries', ax=ax, legend=False)

# Aesthetics
plt.title('Global Crop Production Trends in Agriculture')
plt.xlabel('Number of Countries')
plt.ylabel('Crop Production (million metric tons)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# If the text length of the label is too long, rotate the labels
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/102.png', format='png')

# Clear the current image state
plt.clf()
