
import matplotlib.pyplot as plt 
import pandas as pd 

# Read Data 
data = {'Country': ['USA', 'Canada', 'Mexico', 'Brazil'], 'Number of Tourists': [2000000, 3000000, 1500000, 1000000], 'Average Spend(dollars)': [150, 175, 125, 200]}
df = pd.DataFrame(data)

# Plot the figure 
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(df['Country'], df['Number of Tourists'], label='Number of Tourists', marker='o', color='b')
ax.plot(df['Country'], df['Average Spend(dollars)'], label='Average Spend(dollars)', marker='o', color='r')

# Format the figure 
ax.set_title('International Tourism Trends in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Tourists/Average Spend(dollars)')
ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1.0))
ax.tick_params(axis='x', rotation=45, labelsize=10, labelrotation=45, labelcolor='black')
plt.xticks(df['Country'])
plt.tight_layout()

# Save figure 
plt.savefig('line chart/png/398.png') 
plt.clf()