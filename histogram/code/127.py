import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data_labels = ['Crop Production (million metric tons)']
line_labels = [
    'Wheat', 'Corn', 'Rice', 'Soybean', 
    'Potatoes', 'Tomatoes', 'Lettuce', 
    'Apples', 'Grapes'
]
data = [115, 150, 200, 170, 80, 45, 30, 40, 60]

# Transform the data as needed by seaborn
df = dict(zip(line_labels, data))
df = [(k, v) for k, v in df.items()]

# Create the figure and the axes
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Plot horizontal bar plot
sns.barplot(
    x=[i[1] for i in df],
    y=[i[0] for i in df],
    palette=sns.color_palette("viridis", len(df)),
    orient='h'
)

# Add grid
plt.grid(True, axis='x')

# Set title and labels with wrap for long text
ax.set_title('Regional Crop Production Volumes in Agriculture')
ax.set_xlabel(data_labels[0])
ax.set_ylabel('Crops')
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Auto-resize layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/127.png')

# Clear the current figure state to prevent overlap with future plots
plt.clf()
