
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Media Coverage', 'Ticket Sales', 'Merchandise Sales', 'Public Interest', 'Sponsorship Deals']
data = [19, 20, 30, 15, 16]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,autopct='%1.1f%%', colors=['#FFCCCC', '#FFFF99', '#CCFFCC', '#FF99FF', '#CCFFFF'])
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="upper left")
plt.title('Sports and Entertainment Industry Trends - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_83.png')
plt.clf()