import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data
data_labels = ['Number of Patients (Thousands)']
line_labels = ['General Practice', 'Dental Care', 'Specialist Consultation',
               'Vision and Audiology', 'Physical Therapy', 'Alternative Medicine', 'Psychiatric Services']
data = [300, 400, 500, 200, 150, 100, 50]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plotting
plt.figure(figsize=(12, 8))
ax = plt.subplot()

sns.barplot(x=data_labels[0], y=df.index, data=df, orient='h', palette='viridis')

# Styling
ax.set_title("Utilization of Healthcare Services by Patient Volume", fontsize=16)
ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel('Type of Service', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=12)

# Grid
ax.grid(which='major', axis='x', linestyle='-', linewidth='0.5', color='gray')
ax.set_axisbelow(True)

# Tight layout and save figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/188.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
