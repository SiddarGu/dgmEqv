
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["TV Viewership","Ticket Sales","Merchandising","Digital Content","Sponsorships"]
line_labels = ["Category"]
data = np.array([30,15,10,35,10])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.pie(data, labels = data_labels, startangle=90, counterclock=False, colors=['tab:blue','tab:orange','tab:green','tab:red','tab:purple'], textprops={'wrap':True, 'rotation': 30})
circle = plt.Circle((0,0), radius=0.7, color='white')
ax.add_artist(circle)
ax.set_title('Sports and Entertainment Industry Trends - 2023', fontsize = 14)
plt.legend(data_labels,loc="lower left", bbox_to_anchor=(-0.1, -0.2, 1.2, 0), 
           ncol=2, shadow=True, title="Category", fancybox=True)
plt.grid(True, linestyle='-.')
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_11.png")
plt.clf()