
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Criminal Cases', 'Civil Cases', 'Employment Cases', 'Property Rights Cases', 'Human Rights Cases']
data = [0.22, 0.39, 0.17, 0.15, 0.07]
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(10,7))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')
circle = plt.Circle(xy=(0,0), radius=0.7, color='white')
ax.add_artist(circle)
ax.set_title('Legal Caseload Overview - 2023')
ax.legend(title='Category', loc='upper left')
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_16.png')
plt.clf()