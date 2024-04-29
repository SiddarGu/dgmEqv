
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels=np.array(['Donations','Fundraising','Financial Management','Volunteerism','Public Relations']) 
data=np.array([54,16,11,9,10])
line_labels=np.array(['Category','ratio'])

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)

ax.pie(data, startangle=90, counterclock=False, colors=['red','green','blue','yellow','orange'])
ax.add_artist(plt.Circle((0,0),0.7,color='white'))
ax.legend(data_labels, loc='center right', bbox_to_anchor=(1.5, 0.5))
ax.set_title('Nonprofit Organization Financial Overview - 2023', fontsize=14)
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_3.png')
plt.clf()