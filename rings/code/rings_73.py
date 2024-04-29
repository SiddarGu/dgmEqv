

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Fundraising','Grants','Donations','Volunteering']
data = [50,25,15,10]
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize = (10,6))
ax.pie(data, startangle = 90, counterclock = False)
plt.Circle((0,0), 0.7, color='white')
ax.add_artist(plt.Circle((0,0), 0.7, color='white'))
ax.legend(data_labels)
plt.title('Nonprofit Resource Allocation - 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_141.png')
plt.clf()