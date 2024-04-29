
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Donations","Volunteers","Fundraising","Grants","Charitable Programs"] 
line_labels = ["Category","ratio"] 
data = np.array([[38,20,15,17,10]])

fig, ax = plt.subplots(figsize=(8,6))
ax.set_title("Charitable Contributions - 2021") 
ax.pie(data[0], labels=data_labels, startangle=90,counterclock=False)
c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_116.png")
plt.clf()