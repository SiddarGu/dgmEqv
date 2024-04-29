import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Number of Cases']
line_labels = ['Civil', 'Criminal', 'Corporate', 'Family', 'Intellectual Property', 'Employment', 'Environmental', 'International', 'Traffic']
data = [262, 198, 135, 158, 109, 87, 56, 38, 72]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and add subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plot horizontal bar chart
df.plot(kind='barh', legend=False, ax=ax, color='skyblue', edgecolor='black')

# Apply settings
ax.set_title('Annual Case Volume by Type in the Legal System')
ax.set_xlabel('Number of Cases')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlim(0, max(data) + 10)  # Set x-axis limit slightly larger than the max value for visual appeal

# Rotate labels if necessary and use tight_layout
plt.xticks(rotation=45)
plt.yticks(wrap=True)
plt.tight_layout()

# Save the plot as a PNG image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/610.png'
plt.savefig(save_path)

# Clear the current figure state to prevent replotting of the same data
plt.clf()
