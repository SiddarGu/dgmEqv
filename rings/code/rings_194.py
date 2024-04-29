
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels=['Donations','Fundraising','Grants','Sponsorships','Impact']
line_labels=['Category','ratio']
data = np.array([['Donations',38],['Fundraising',30],['Grants',12],['Sponsorships',7],['Impact',13]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
ax.pie(data[:,1].astype(float), labels=data[:,0], autopct='%1.1f%%', startangle=90, colors=colors, shadow=True, textprops={'fontsize': 14})
circle=plt.Circle((0,0), 0.70, color='white')
ax.add_artist(circle)
ax.legend(data_labels,loc='best', fontsize=18)
ax.set_title('Nonprofit Performance Overview - 2023', fontsize=22)
plt.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_43.png')
plt.clf()