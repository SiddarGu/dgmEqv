
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Stocks','Bonds','Mutual Funds','Options','Futures','Derivatives','Forex']
data = [400,500,700,250,150,100,200]
line_labels = ['Number of Investors']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], align='center', width=sector_angle, label=data_labels[i], alpha=0.5)

ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels)+1)[:-1])
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=45)
ax.set_ylim(0, np.max(data)+50)
ax.legend(bbox_to_anchor=(1.3, 1.0))
ax.set_title('Investor Participation in Different Financial Instruments in 2021', fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_90.png')

plt.clf()