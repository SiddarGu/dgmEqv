import matplotlib.pyplot as plt
import squarify

# Raw data
data_content = """Platform,User Engagement (%)
Facebook,25
YouTube,20
Instagram,15
Twitter,14
LinkedIn,10
Pinterest,7
Reddit,5
Snapchat,4"""

# Process raw data
rows = data_content.split("\n")
data_labels = rows.pop(0).split(",")[1:]  # Removing 'Platform' and getting ['User Engagement (%)']

line_labels = []
data = []
for row in rows:
    platform, engagement = row.split(",")
    line_labels.append(platform)
    data.append(int(engagement))

# Plotting treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral_r([(d - min(data)) / float(max(data) - min(data)) for d in data])  # Color spectrum
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':9, 'wrap': True})

plt.title("User Engagement Across Major Social Media Platforms")
plt.axis('off')  # Remove the axes
plt.tight_layout()  # Automatically resize

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/290.png"
plt.savefig(save_path)

# Clear the current figure state
plt.clf()