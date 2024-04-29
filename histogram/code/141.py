import pandas as pd
import matplotlib.pyplot as plt

# Define data
data_labels = ["Number of Cases"]
line_labels = [
    "Heart Disease",
    "Cancer",
    "Diabetes",
    "Respiratory Diseases",
    "Infectious Diseases",
    "Mental Disorders",
    "Neurological Disorders",
    "Digestive Disorders",
    "Injuries"
]
data = [7.2, 6.8, 4.1, 3.9, 3.0, 2.5, 1.8, 1.6, 1.2]

# Use pandas to create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure
fig = plt.figure(figsize=(12, 8))  # Set to a larger figure size to prevent content overflow
ax = fig.add_subplot(111)

# Plot the horizontal bar chart
df.plot(kind='barh', ax=ax, legend=False, grid=True, color='skyblue')

# Format the chart to make it clear and intuitive
ax.set_title('Prevalence of Common Diseases per 1000 Individuals')
ax.set_xlabel('Number of Cases per 1000 Individuals')
for i, v in enumerate(data):
    ax.text(v + 0.1, i, str(v), color='blue', va='center')

# If the label text is too long, rotate or wrap it
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Automatically resize the layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1005.png', format='png')

# Clear the current image state after saving
plt.clf()
