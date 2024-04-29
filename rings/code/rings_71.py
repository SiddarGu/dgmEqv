
import matplotlib.pyplot as plt
import pandas as pd

data_labels = ['Donations', 'Fundraising', 'Volunteers', 'Grants']
data = [25, 20, 40, 15]
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(8, 8))

patches, texts, autotexts = ax.pie(data, startangle=90, counterclock=False, autopct='%.f%%', colors=['#20d526', '#3c20d5', '#d5203c', '#d5bb20'])

for text in texts:
    text.set_wrap(True)

centre_circle = plt.Circle((0,0),0.50,fc='white')

ax.add_artist(centre_circle)

ax.legend(data_labels, bbox_to_anchor=(1.3,0.8))
ax.grid(True)
ax.set_title('Charitable Contributions Overview - 2023')

plt.tight_layout()

plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_14.png')

plt.clf()