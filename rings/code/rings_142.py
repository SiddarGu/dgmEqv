
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data_labels=['Crop Yield','Irrigation','Nutrition','Livestock Production']
data=np.array([[40,20,15,25]])
line_labels=['Category']

# Create figure 
fig, ax = plt.subplots(figsize=(10,10))

# Create pie chart
wedges, texts, autotexts = ax.pie(data[0], labels=data_labels,
                                 autopct='%1.1f%%', radius=1, pctdistance=0.85, 
                                 startangle=90, counterclock=False)

# Create white circle
white_circle = mpatches.Circle((0,0),0.7,fc='white')
ax.add_artist(white_circle)

# Set legend
ax.legend(data_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Set title
ax.set_title('Agricultural Production Trends - 2023', fontsize=16)

# Rotation of the labels
plt.setp(autotexts, fontsize=12, rotation=45, ha="right", va="center")
 
# Automatically tight layout
plt.tight_layout()

# Save chart
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_102.png') 

# Clear the current image state
plt.clf()