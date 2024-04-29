import pandas as pd
import matplotlib.pyplot as plt

# Data setup
data_labels = ["Number of Exhibits", "Visitors (Thousands)"]
data = {
    "Exhibit Type": ["Photography", "Sculpture", "Painting", "Digital Art",
                     "Performance Art", "Classical Art", "Modern Art"],
    "Visitors (Thousands)": [18.7, 24.3, 30.6, 12.4, 22.8, 14.5, 26.1]
}

# Transforming data into a DataFrame
df = pd.DataFrame(data)

# Setting the figure and axes
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Creating the histogram
df.plot(kind="bar", x="Exhibit Type", y="Visitors (Thousands)",
        ax=ax, color='skyblue', grid=True, legend=False)

# Title and labels
plt.title('Visitor Distribution Across Different Art Exhibit Types')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Rotate labels if they're too long
plt.xticks(rotation=45, ha="right", wrap=True)

# Ensuring the layout fits well and labels are not overlapping
plt.tight_layout()

# Save figure 
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/123.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
