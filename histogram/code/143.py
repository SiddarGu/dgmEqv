import pandas as pd
import matplotlib.pyplot as plt

# Data parsing and transformation
raw_data = "BMI Classification,Number of Patients (Thousands)/n " \
           "Underweight (<18.5),25/n Normal weight (18.5-24.9),200/n " \
           "Overweight (25-29.9),150/n Obesity I (30-34.9),120/n " \
           "Obesity II (35-39.9),90/n Extreme Obesity III (≥40),60"

# Split the string into lines
lines = raw_data.split('/n ')

# Extract labels for data
data_labels = lines[0].split(',')

# Extract labels for lines and the data itself
line_labels = []
data = []
for line in lines[1:]:
    label, value = line.rsplit(',', 1)
    line_labels.append(label)
    data.append(int(value))

# Convert to DataFrame for plotting
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Create figure and plot horizontal bar chart (histogram)
plt.figure(figsize=(10, 6))
ax = plt.subplot()
df.plot(kind='barh', legend=False, ax=ax, color='#1f77b4')

# Customizing the plot to make it intuitive
plt.title('Patient Distribution by BMI Classification in Healthcare Data')
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[0])
plt.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
plt.tight_layout()

# Ensure the y-axis labels' full text is shown
ax.yaxis.get_label().set_wrap(True)
ax.set_yticklabels(line_labels, rotation=0)

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/143.png', format='png')

# Clear the current image state at the end of the code
plt.clf()
