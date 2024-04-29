
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

data_labels = ['Donation','Community Service','Fundraising','Advocacy','Volunteering']
data = [25,19,27,14,15]
line_labels = ['Category','Ratio']

fig,ax = plt.subplots(figsize=(8, 8))
ax.pie(data, startangle=90, counterclock=False,
       labeldistance=0.7, autopct='%1.1f%%', textprops={'fontsize': 10})

c = Circle((0,0), 0.4, facecolor='white',edgecolor='black', linewidth=2)
ax.add_artist(c)

ax.legend(data_labels, loc='upper left', bbox_to_anchor=(0.9, 0.9), fontsize=10)

ax.set_title('Impact of Charity and Nonprofit Organizations - 2023', fontsize=12)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_30.png')
plt.clf()