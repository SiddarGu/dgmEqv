

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Employment Status':['Full-Time Employees', 'Part-Time Employees', 'Contractors', 'Freelancers'], 
                   'Percentage':[55,30,10,5]})

# Create the figure
plt.figure(figsize=(8,8))

# Plot the data
plt.pie(df['Percentage'], labels=df['Employment Status'], autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8},
        wedgeprops={'linewidth': 1, 'edgecolor': 'black'}, rotatelabels=True, pctdistance=0.7, radius=1)

# Add a legend
plt.legend(df['Employment Status'],loc='lower right', bbox_to_anchor=(1.2, 0.5, 0.5, 0.5))

# Set the title
plt.title('Distribution of Employee Types in the USA in 2023', fontsize=14)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/331.png')

# Clear the image
plt.clf()