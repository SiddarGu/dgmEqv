import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data processing
data_labels = ['Number of Cases']
line_labels = ['Heart Disease', 'Cancer', 'Diabetes', 'Respiratory Diseases', 'Infectious Diseases',
               'Mental Health Disorders', 'Neurological Disorders', 'Digestive Diseases', 'Injuries']
data = np.array([250, 230, 180, 150, 120, 90, 80, 70, 60])

# Creating a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Setting up the plot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plotting the histogram using seaborn
sns.barplot(x=df.index, y=df['Number of Cases'], palette='viridis', ax=ax)

# Adding the grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Rotating the x-axis labels if needed
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right")

# Setting the title
plt.title('Prevalence of Common Health Conditions in a Population')

# Automatically adjusts subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/133.png'
plt.savefig(save_path, dpi=100)  # You can adjust the dpi for higher resolution if needed

# Clear the current figure's state to prevent re-plotting
plt.clf()
