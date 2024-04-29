
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# transform data
data_labels = ['Vaccinations', 'Infection Control', 'Diagnostics', 'Treatment Standards', 'Patient Safety']
line_labels = ['Category', 'ratio']
data = [['Vaccinations', 32], ['Infection Control', 16], ['Diagnostics', 22], ['Treatment Standards', 20], ['Patient Safety', 10]] 

# plot data
plt.figure(figsize=(10, 8))
ax = plt.subplot()
ax.pie([_[1] for _ in data], labels=[*[f'{_[0]}\n{_[1]}%' for _ in data]], startangle=0, counterclock=False, wedgeprops = {'linewidth': 1, 'edgecolor': 'black'}, 
        colors=[*['#1f77b4', '#aec7e8', '#ffbb78', '#ff7f0e', '#2ca02c']])
circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(circle)
plt.title('Healthcare Quality Metrics - 2023', fontsize=15)
ax.legend(data_labels, loc='upper left')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_62.png',dpi=300)
plt.clf()