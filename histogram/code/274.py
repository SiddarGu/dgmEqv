import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data preparation
data_labels = ['Number of Individuals']
line_labels = ['Underweight (<18.5)', 'Normal (18.5-24.9)', 'Overweight (25-29.9)', 
               'Obese I (30-34.9)', 'Obese II (35-39.9)', 'Extreme Obesity (>40)']
data = np.array([12, 30, 45, 25, 15, 8])

# Setting up the plot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the data
sns.barplot(x=data, y=line_labels, ax=ax)

# Customizing the plot
ax.set_title('Prevalence of BMI Categories in a Health Survey', fontsize=14)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel('BMI Category', fontsize=12)
plt.xticks(np.arange(0, max(data)+1, 5))
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)
ax.xaxis.tick_top()

# Adjusting label orientation and style if necessary
ax.set_yticklabels(labels=line_labels, rotation=0, wrap=True)

# Resizing the layout and saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/624.png', dpi=300)

# Clearing the current figure state
plt.clf()
