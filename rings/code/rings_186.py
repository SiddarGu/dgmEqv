
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Donations', 'Grants', 'Community Service', 'Fundraising', 'Volunteering']
data = np.array([30, 10, 15, 20, 25])
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.set_title('Charity and Nonprofit Organizations Performance - 2023')
ax.pie(data, startangle=90,counterclock=False, labels=data_labels, colors=[
        '#FF4D4F', '#E74292', '#00A8C6', '#2ECC71', '#F1C40F'])
c = plt.Circle((0, 0), 0.70, color='white')
ax.add_artist(c)
ax.legend(data_labels, loc="best")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_32.png")
plt.clf()