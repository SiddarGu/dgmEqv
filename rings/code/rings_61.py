
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Air Transport', 'Road Transport', 'Sea Transport', 'Logistics Services', 'Warehousing']
data = np.array([11, 23, 20, 22, 24])
line_labels = ['Mode', 'Ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#3399FF', '#FF6600', '#009933', '#9900CC', '#FF6600'])

centre_circle = plt.Circle((0,0),0.5,color='white', fc='white',linewidth=1.25)
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="best")
ax.set_title('Transportation and Logistics Overview - 2023', fontsize=14)
ax.grid(axis='both', linestyle='-.')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_127.png', dpi=300)
plt.clf()