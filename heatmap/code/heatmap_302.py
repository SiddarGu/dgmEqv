
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set data
category = ['Telecommunications', 'Software & IT Services', 'Electronics & Semiconductors', 'E-commerce & Online Services', 'Hardware & Devices', 'Networking & Internet Services', 'Big Data & Analytics', 'Gaming & Entertainment', 'Artificial Intelligence & Machine Learning']
patents = [750, 850, 950, 550, 500, 350, 450, 300, 400]
cybersecurity = [60, 30, 25, 15, 20, 35, 20, 15, 25]
cloud_computing = [40, 45, 35, 25, 30, 40, 15, 40, 30]
artificial_intelligence = [25, 35, 40, 20, 15, 10, 30, 25, 25]
virtual_reality = [15, 10, 20, 30, 25, 25, 25, 30, 20]
internet_of_things = [20, 25, 15, 35, 20, 30, 20, 10, 35]

# Create dictionary
data = {'Category': category, 'Patents': patents, 'Cybersecurity': cybersecurity, 'Cloud Computing': cloud_computing, 'Artificial Intelligence': artificial_intelligence, 'Virtual Reality': virtual_reality, 'Internet of Things': internet_of_things}

# Create dataframe
df = pd.DataFrame(data).set_index('Category')

# Plot chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=0.5, center=df.loc[:, 'Patents'].mean())

# Set ticks and ticklabels
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set title
ax.set_title('Technology and Internet Trends by Category')

# Automatically resize image and save chart
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_4.png', bbox_inches='tight')

# Clear current image state
plt.clf()