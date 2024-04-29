import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_values = """
0-4,4.2
5-12,2.5
13-18,1.8
19-30,1.4
31-45,2.2
46-60,3.5
61-75,5.9
76+,7.8
"""

# Transform the given data into three variables: data_labels, data, line_labels
data_lines = data_values.strip().split('\n')
data_labels = ['Age Bracket (Years)', 'Average Hospital Visits per Person']
line_labels, data = zip(*(line.split(',') for line in data_lines))
data = [float(d) for d in data]

# Create a DataFrame
df = pd.DataFrame({'Age Bracket (Years)': line_labels, 'Average Hospital Visits per Person': data})

# Plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Create histogram using 'pandas'
df.plot(kind='bar', x='Age Bracket (Years)', y='Average Hospital Visits per Person', ax=ax, legend=False)

# Setting the title
ax.set_title('Average Hospital Visits Per Person by Age Bracket')

# Enhancing visual appearance
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_xticklabels(df['Age Bracket (Years)'], rotation=45, ha="right", wrap=True)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1009.png', format='png')

# Clear the current figure state
plt.clf()
