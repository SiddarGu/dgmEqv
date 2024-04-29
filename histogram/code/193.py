import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data with newline characters as a delimiter
raw_data = """Energy Production (TWh),Country
50,Tanzania
100,Kenya
150,Ghana
200,Morocco
250,Nigeria
300,South Africa
350,Egypt
400,Algeria
450,Libya"""

# Parsing the data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1]  # Assuming "Energy Production (TWh)" is not used
line_labels = [line.split(',')[1] for line in lines[1:]]
data = [int(line.split(',')[0]) for line in lines[1:]]  # Assume this is categorical data for the histogram
df = pd.DataFrame(data, index=line_labels, columns=['Energy Production (TWh)'])

# Visualizing the data as a horizontal histogram
sns.set_style("whitegrid")
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create the horizontal bar plot
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Customizing the plot
ax.set_title('Energy Production Range by Country in Africa', fontsize=16)
ax.set_xlabel('Energy Production (TWh)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_train/193.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state to prevent interference with future plots
plt.clf()
