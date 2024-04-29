import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data in raw format
raw_data = """0-1,150
1-5,300
5-10,500
10-20,400
20-30,200
30-40,100
40-50,50
50-100,25
100+,10"""

# Parsing the raw_data into lists for labels and data
lines = raw_data.split('\n')
data_labels = ["Traffic Range (Millions of Visits)", "Number of Websites"]
line_labels, data = zip(*[line.split(',') for line in lines])

# Converting data to numerical format
data = [int(value) for value in data]

# Creating a DataFrame for visualization
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Seaborn style
sns.set_style('whitegrid')

# Create the figure and axis
plt.figure(figsize=(12, 8))
ax = sns.barplot(x="Traffic Range (Millions of Visits)", y="Number of Websites", data=df, palette="viridis")

# Title and labels
ax.set_title("Web Traffic Distribution Across Various Websites")
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right", wrap=True)

# Tight layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/600.png')

# Clear the current figure
plt.clf()
