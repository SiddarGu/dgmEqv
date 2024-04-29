

import matplotlib.pyplot as plt
import numpy as np 

# Create data 
Age_Group = np.array(['18-25','26-35','36-45','46-55','56-65','66-75','76-85'])
Happiness_Score = np.array([7.2,7.5,7.7,8.0,7.8,7.2,6.5])
Life_Satisfaction_Score = np.array([6.8,7.2,7.5,7.7,7.5,6.8,6.2])

# Create figure and plot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(Age_Group, Happiness_Score, 'g-',label='Happiness Score')
ax.plot(Age_Group, Life_Satisfaction_Score, 'b--',label='Life Satisfaction Score')

# Set labels and title
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Score (out of 10)', fontsize=12)
ax.set_title('Age-related Happiness and Life Satisfaction Scores in 2021', fontsize=14)

# Set ticks and grid
ax.set_xticks(Age_Group)
ax.grid(linestyle='-.')

# Set legend, set outside of the figure and not interfere with the chart
ax.legend(loc='center left', bbox_to_anchor=(1,0.5), fontsize=12)

# Adjust the spacing of the subplots and display the figure
plt.tight_layout()
plt.savefig('line chart/png/487.png')

plt.clf()