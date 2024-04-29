import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ["Disease Incidence Rate (per 100,000)", "Number of Cases"]
line_labels = [
    "Heart Disease",
    "Cancer",
    "Stroke",
    "Diabetes",
    "Respiratory Disease",
    "Alzheimer's",
    "Influenza",
    "Kidney Disease"
]
data = [250, 200, 150, 175, 125, 100, 75, 50]

# Creating a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=["Number of Cases"])

# Creating figure and adding a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting horizontal histogram
df.plot(kind='barh', legend=False, ax=ax, color='skyblue')

# Styling the plot
ax.set_xlabel(data_labels[0])
ax.set_title('Prevalence of Common Diseases in the Population')
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.tick_params(axis='y', which='major', labelsize=10)

# If the text length of label is too long, use the parameter "rotation" or "wrap=True"
plt.setp(ax.get_yticklabels(), wrap=True)

# Resize the image using tight_layout()
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/163.png')

# Clear the current image state
plt.clf()
