import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Unpack the data
data_labels = ["Percentage of Population (%)"]
line_labels = [
    "Less than High School",
    "High School Graduate",
    "Some College",
    "Bachelor's Degree",
    "Postgraduate Degree",
    "Doctorate",
    "Professional Degree"
]
data = [12.3, 30.5, 21.7, 18.2, 9.4, 3.9, 4.0]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Initialize the figure and add a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create horizontal bar plot
sns.barplot(x=data_labels[0], y=df.index, data=df, orient='h', palette='viridis')

# Set the chart title and labels
plt.title('Educational Attainment of the Population')
plt.xlabel('Percentage of Population (%)')

# Improve layout to fit everything and prevent overlapping text
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/66.png'
plt.savefig(save_path)

# Clear the current figure state to prevent reuse
plt.clf()
