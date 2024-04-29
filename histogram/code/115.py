import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    "Age Range": ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "90+"],
    "Number of Hospital Visits (Thousands)": [120, 110, 105, 115, 130, 150, 170, 160, 140, 100]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a figure before plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a histogram using 'pandas' plot() function
df.plot(kind='bar', x='Age Range', y='Number of Hospital Visits (Thousands)',
        ax=ax, color='skyblue', edgecolor='black')

# Set a title
ax.set_title('Hospital Visit Frequency by Age Groups')

# Adding grid lines
ax.grid(axis='y')

# To prevent long label texts from overlapping, rotate the labels
ax.set_xticklabels(df['Age Range'], rotation=45)

# Automatically adjust subplot params for the figure to fit into the canvas
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/115.png')

# Clear the current image state
plt.clf()
