
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dataframe
data = {'Year':[2017, 2018, 2019, 2020],
        'Employee Satisfaction Index':[80, 85, 90, 93],
        'Employee Retention Rate':[90, 91, 93, 94],
        'Average Salary':[50000, 54000, 58000, 60000]
       }
df = pd.DataFrame(data)

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Plot line chart
ax.plot(df['Year'], df['Employee Satisfaction Index'], label='Employee Satisfaction Index', marker='o')
ax.plot(df['Year'], df['Employee Retention Rate'], label='Employee Retention Rate', marker='o')
ax.plot(df['Year'], df['Average Salary'], label='Average Salary', marker='o')

# Set title 
fig.suptitle('Employee Job Satisfaction and Retention Rate in the US from 2017-2020', fontsize=20)

# Set x-axis label
ax.set_xlabel("Year", fontsize=15)

# Set y-axis label
ax.set_ylabel("Index/Rate/Salary", fontsize=15)

# Set x-axis tick
ax.set_xticks(df['Year'])

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fontsize=15, ncol=3)

# Adjust figure
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the image
plt.savefig('line chart/png/330.png')

# Close the figure
plt.clf()