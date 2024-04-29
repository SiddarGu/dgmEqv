import matplotlib.pyplot as plt
import seaborn as sns

# Given data in the form of a string
raw_data = """Case Type,Number of Cases
Civil,1450
Criminal,1230
Family,870
Tax,650
Environmental,430
Corporate,520
Intellectual Property,310
Bankruptcy,290
International,210"""

# Parsing the data
data = []
line_labels = []
for line in raw_data.split("\n")[1:]:  # Skip header line
    label, count = line.split(",")
    line_labels.append(label)
    data.append(int(count))

# Labels for each column (only one column in this case)
data_labels = ["Number of Cases"]

# Create figure and axis with larger figsize to prevent overlapping labels
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create horizontal histogram
sns.barplot(x=data, y=line_labels)

# Set the title
plt.title('Number of Legal Cases by Type')

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Automatically adjust subplot params for the figure to fit into
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/134.png', format='png')

# Clear the current figure state to prevent re-plotting upon re-run
plt.clf()
