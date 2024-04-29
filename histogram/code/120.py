import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Number of Patients']
line_labels = ['Normal (<120/80)', 'Elevated (120-129/<80)', 'Hypertension Stage 1 (130-139/80-89)',
               'Hypertension Stage 2 (140-179/90-119)', 'Hypertensive Crisis (>=180/>=120)']
data = [[350], [120], [200], [160], [70]]

# Create a pandas DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Visualization
fig = plt.figure(figsize=(12, 6)) # figsize parameter to prevent content from being cramped
ax = fig.add_subplot(111)

# Plot vertical histograms
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Set title and labels
ax.set_title('Patient Distribution by Blood Pressure Categories', pad=20)
ax.set_xlabel('Blood Pressure Categories', labelpad=15)
ax.set_ylabel('Number of Patients', labelpad=15)

# Set x-tick labels with rotation and wrap for better clarity
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right", wrap=True)

# Auto resize the plot layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/120.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state
plt.clf()
