
import matplotlib.pyplot as plt
import pandas as pd

# Create the figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Create dataframe
data = {'Age Groups':['18-24','25-34','35-44','45-54','55-64','65+'],
        'Percentage':[20,30,20,15,10,5]}
df = pd.DataFrame(data)

# Plot the pie chart
ax.pie(df['Percentage'], labels=df['Age Groups'], autopct='%.2f%%', textprops={'fontsize': 15}, 
       wedgeprops={'linewidth': 1, 'edgecolor':'black'}, 
       startangle=90, shadow = True)

# Set the title
ax.set_title('Employee Age Distribution in the USA, 2023', fontsize=20)

# Set the legend position
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 0.8))

# Tighten the layout
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/351.png', dpi=300)

# Clear the figure
plt.clf()