import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Ticket Price Range ($)', 'Number of Events']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250',
               '250-300', '300-350', '350-400', '400-450', '450-500']
data = [220, 180, 140, 90, 70, 50, 30, 20, 10, 5]

# Transforming data into a DataFrame
df = pd.DataFrame({'Ticket Price Range ($)': line_labels, 'Number of Events': data})

# Creating figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Plotting the histogram
df.plot(kind='bar', x='Ticket Price Range ($)', y='Number of Events',
        ax=ax, color='skyblue', grid=True)

# Setting title, labels, and aesthetic enhancements
plt.title('Pricing Trends of Sports and Entertainment Events')
plt.xlabel('Price Range ($)')
plt.ylabel('Number of Events')
plt.xticks(rotation=45, ha='right', wrap=True)

# Resizing figure to fit content neatly
plt.tight_layout()

# Save the figure to the desired path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/38.png'
plt.savefig(save_path, format='png')

# Clearing the current figure
plt.clf()
