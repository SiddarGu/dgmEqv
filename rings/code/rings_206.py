
import matplotlib.pyplot as plt
data_labels = ["Popularity","Quality of Service","Customer Satisfaction","Revenue","Infrastructure"]
data = [25,20,17,26,12]
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(20,10))
ax.pie(data, counterclock=False, startangle=90, autopct='%1.1f%%',
       colors=['red','green','blue','orange','purple'])

circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels)
ax.set_title('Tourism and Hospitality Performance Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_6.png')
plt.clf()