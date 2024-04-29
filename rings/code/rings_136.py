
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy Sources','Oil and Gas','Nuclear Energy','Coal','Investments']
data = np.array([19,35,23,13,10])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
centre_circle = plt.Circle((0,0), 0.75, color='white', fc='white',linewidth=1.25)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="upper right")
plt.title('Energy and Utilities Industry Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_91.png')
plt.clf()